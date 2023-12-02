# Use the official Python image as the base image
FROM python:3.10.8

ENV PIP_ROOT_USER_ACTION=ignore

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the working directory
COPY . /app

# Install the application dependencies
RUN pip install -r requirements.txt

RUN  pip install --upgrade pip
EXPOSE 9000/tcp

# Define the entry point for the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]