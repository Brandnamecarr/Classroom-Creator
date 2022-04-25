import csv
from distutils.log import error
from flask import Flask, render_template, request, session, abort, redirect, jsonify, url_for
from datetime import datetime
import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
from googleapiclient.errors import HttpError
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired
from werkzeug.utils import secure_filename
from classroom import Classroom
from canvasapi import Canvas
from csv_service import CsvDataPoint, csv_service

# needed to imitate https server
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# configuration information needed for google api flow
CLIENT_SECRETS_FILE = "credentials.json"
Scopes = ["https://www.googleapis.com/auth/classroom.courses", "https://www.googleapis.com/auth/classroom.rosters"]

app = Flask(__name__)
app.secret_key = b'_5#y2L"Fsss8z\n\xec]/'

# Global string for csv filename
csvFileName = ""

# Create static/uploadedfiles directory for CSV upload component.
try:
    os.mkdir(os.path.join('static', 'uploadedfiles'))
except:
    pass

# class for uploading a file upload form.
class UploadFileForm(FlaskForm):
    # creates buttons with these names. 
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload")

@app.route("/", methods=['GET', 'POST'])
def home():
    csvUploadSuccess = False
    form = UploadFileForm()

    if 'credentials' not in session:
        return redirect('google_login')
    
    if 'canvas-url' in session and 'canvas-api-key' in session:
        return render_template('index.html', form=form, csvUploadSuccess=csvUploadSuccess, canvas=True)
    elif form.validate_on_submit():
        file = form.file.data # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),os.path.join('static', 'uploadedfiles'), secure_filename(file.filename))) # Then save the file
        csvUploadSuccess = True
        return render_template('index.html', form=form, csvUploadSuccess = csvUploadSuccess, filename=file.filename, canvas=False)
    return render_template('index.html', form=form, csvUploadSuccess=csvUploadSuccess, canvas=False)

####################
##### CSV APIS #####
####################
@app.route("/cancel_csv", methods=['GET', 'POST'])
def cancel_csv():
    if request.method == 'POST':
        post_data = request.form['file']
        os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)),os.path.join('static', 'uploadedfiles'),secure_filename(post_data)))

    return redirect("/")

#############################
##### GOOGLE OAUTH APIS #####
#############################
@app.route("/google_login")
def google_login():
    "loging in page"
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes = Scopes)
    
    flow.redirect_uri = url_for('google_success', _external=True)

    auth_url, state = flow.authorization_url(access_type='offline')

    session['state'] = state
    
    return redirect(auth_url)

@app.route("/google_login_check")
def google_login_check():
    if 'credentials' not in session:
        return "false"
    return "true"

@app.route("/google_success")
def google_success():
    state = session['state']

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=Scopes, state=state)
    flow.redirect_uri = url_for('google_success', _external=True)

    # Use the authorization server's response to fetch the OAuth 2.0 tokens.
    authorization_response = request.url
    flow.fetch_token(authorization_response=authorization_response)

    # Store credentials in the session.
    # ACTION ITEM: In a production app, you likely want to save these
    #              credentials in a persistent database instead.
    credentials = flow.credentials
    session['credentials'] = credentials_to_dict(credentials)

    return redirect("/")

# to be used as
@app.route("/get_current_google_classrooms")
def get_current_google_classrooms():
    creds = google.oauth2.credentials.Credentials(**session['credentials'])
    service = googleapiclient.discovery.build('classroom', 'v1', credentials=creds)
    results = service.courses().list().execute()
    courses = results.get('courses', [])
        
    return jsonify(courses)

@app.route("/google_logout")
def google_logout():
    session.pop('credentials', None)
    return redirect("/google_login")

#############################
##### CANVAS OAUTH APIS #####
#############################
@app.route("/canvas_connect", methods=['GET', 'POST'])
def canvas_connect():
    if request.method == 'POST':
        url = request.form['url']
        api_key = request.form['api-key']
        session['canvas-url'] = url
        session['canvas-api-key'] = api_key
        return redirect('/')

@app.route("/canvas_disconnect")
def canvas_disconnect():
    session.pop('canvas-url', None)
    session.pop('canvas-api-key', None)
    return redirect('/')

@app.route("/get_canvas_courses_names")
def get_course_names():
    courses = get_canvas_courses()
    result = []
    for course in courses:
        result.append({
            'course_name' : course.course_name,
            'course_section' : course.course_section})
    
    return jsonify(result)

def get_canvas_courses():
    canvas_api = Canvas(session['canvas-url'], session['canvas-api-key'])
    tmp_courses = canvas_api.get_courses()
    courses = []
    for course in tmp_courses:
        sections = course.get_sections()
        users = course.get_users()
        for sec in sections:
            students = [x.user['id'] for x in (sec.get_enrollments(type=['StudentEnrollment']))]
            emails = []
            for user in users:
                if user.id in students:
                    emails.append(user.email)
            
            courses.append(Classroom(course.name, sec.name, emails))
    
    return courses

def upload_courses_to_google(courses):
    creds = google.oauth2.credentials.Credentials(**session['credentials'])
    service = googleapiclient.discovery.build('classroom', 'v1', credentials=creds)

    for course in courses:
        # create course
        body = course.create_course_format()
        g_course = service.courses().create(body=body).execute()
        # enroll students to course
        students = course.enroll_students_format(g_course.get('id'))
        for s in students:
            print(s)
            g_student = service.invitations().create(body=s).execute()


########################
##### Migrate APIs #####
########################

@app.route("/migrate_canvas")
def migrate_canvas():
    # security feature to prevent users bypassing logins
    if 'credentials' not in session:
        return redirect('google_login')
    elif 'canvas-url' not in session and 'canvas-api-key' not in session:
        return redirect('/')
    
    # gather classroom objects of canvas courses
    courses = get_canvas_courses()

    try:
        upload_courses_to_google(courses)
    except HttpError as error:
        print(error)

    return "success"

@app.route("/migrate_csv")
def migrate_csv():
    # initializing empty lists for the course information and list of students that will be received from a .CSV.
    courseInfo = []
    students = []
    # security feature to prevent users bypassing logins
    if 'credentials' not in session:
        return redirect('google_login')
    
    # gets the filename of the .csv in the static/uploadedfiles folder.
    tmp = makeCsvFilename()
    csvObject = csv_service(tmp)

    # gather classroom objects of courses from csv
    courseInfo, students = csvObject.get_from_csv()
    courseName = courseInfo[0]
    courseSection = courseInfo[1]
    newClass = []
    # append new classroom as a list of size 1 to ship to Gooogle Classroom.
    newClass.append(Classroom(courseName, courseSection, students))

    try:
        upload_courses_to_google(newClass)
    except HttpError as error:
        print(error)
        return "failure"

    # call the cleanup() function to remove the .csv file from the static/uploadedfiles folder.
    # helps reset the filename variable.
    cleanOutUploadsFolder(tmp)
    return "success"

###########################
##### OTHER PAGE APIS #####
###########################

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/docs")
def docs():
    return render_template('docs.html')

############################
##### HELPER FUNCTIONS #####
############################

# goes into the static/uploadedfiles directory.
# only 1 .csv file will be there (going to implement a cleanup function).
# get the name of that file, set it as the global csvFileName variable.
def makeCsvFilename():
    path = os.path.join('static', 'uploadedfiles')
    files = os.listdir(path)
    print(files)
    path = path + "/"
    for file in files:
        path = path + file
    csvFileName = path
    return csvFileName

# deletes the uploaded .csv file.
# prevents multiple uploads of the same file.
def cleanOutUploadsFolder(path):
    try:
        os.remove(path)
    except OSError as e:
        print("Error: {} : {}.".format(path, e.strerror))
    
    csvFileName = ""

def credentials_to_dict(credentials):
  return {'token': credentials.token,
          'refresh_token': credentials.refresh_token,
          'token_uri': credentials.token_uri,
          'client_id': credentials.client_id,
          'client_secret': credentials.client_secret,
          'scopes': credentials.scopes}


###################################
##### APPLICATION ENTRY POINT #####
###################################

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)