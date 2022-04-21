#Create Ubuntu image with python 3.8
FROM python:3.8-slim-buster

# working dir
WORKDIR /app

COPY . .

#Install dependencies
RUN apt-get -y update
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]