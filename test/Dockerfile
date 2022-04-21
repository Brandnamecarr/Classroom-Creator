#Create Ubuntu image with python 3.8
FROM python:3.8

# working dir
WORKDIR /

COPY . .

#Install dependencies
RUN apt-get -y update
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt

#Expose required port
EXPOSE 5000

CMD gunicorn app:app