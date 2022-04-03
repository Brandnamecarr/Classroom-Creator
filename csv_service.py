import csv
# class for creating a student
# will have to change based on the format of canvas data (what gets passed in).
class CsvDataPoint:
    def __init__(self, email) -> None:
        self.email = email
    
# csv_service, reads a CSV file from data.
class csv_service:
    def __init__(self, filename):
        self.filename = filename
    
    # CSV Import
    # Returns 2 lists: a list of the Class-Data: [ID, Class, Instructor]
    #                  a list of the Students: [Email]
    def get_from_csv(self):
        students_from_csv = [] # empty list of students.
        classDataRaw = []

        with open(self.filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            reader.__next__() # skip headers.
            for row in reader:
                if row[0].isdigit():
                    classDataRaw.append(row)
                else:
                    students_from_csv.append(CsvDataPoint(row[0]))
        
        classData = []
        classData.append(classDataRaw[0][0])
        classData.append(classDataRaw[0][1])
        classData.append(classDataRaw[0][2])

        return classData, students_from_csv