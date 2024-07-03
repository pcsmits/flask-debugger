FROM python:3

#Set the working directory in the Docker container
WORKDIR /app

#Copy the dependencies file to the working directory
COPY requirements.txt .
COPY Dockerfile .

#Install the dependencies
RUN pip install -r requirements.txt

#Copy the Flask app code to the working directory
COPY src/ .

ENV ENVIRONMENT development

#Run the container
CMD [ "python", "./app.py" ]
