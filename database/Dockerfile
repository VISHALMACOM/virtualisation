# Use an official Python runtime as the base image
FROM python:3.9
RUN mkdir -p /Student
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /Student

# Copy the requirements file and install dependencies
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install psycopg2-binary

# Expose the port that the Django app will run on
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "./Student/manage.py", "makemigrations"]
CMD ["python", "./Student/manage.py", "sqlmigrate", "./Student/management", "0001"]
CMD ["python", "./Student/manage.py", "migrate"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "./Student/manage.py", "runserver", "0.0.0.0:8000"]
