# Use an official Python runtime as the base image
FROM python:3.9
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Copy the requirements file and install dependencies
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Install the wait-for-it script
#RUN apt-get update && apt-get install -y --no-install-recommends \
#    netcat-traditional \
#    && rm -rf /var/lib/apt/lists/*
#COPY wait-for-it.sh /usr/local/bin/
#RUN chmod +x /usr/local/bin/wait-for-it.sh

# Expose the port that the Django app will run on
EXPOSE 8000

# Command to wait for the database to be ready and then run migrations and start the Django server
#CMD ["wait-for-it.sh", "db:3306", "--", "python", "manage.py", "makemigrations"]
#CMD ["wait-for-it.sh", "db:3306", "--", "python", "manage.py", "migrate"]
#CMD ["wait-for-it.sh", "db:3306", "--", "python", "manage.py", "migrate"]
CMD ["python", "./Student/manage.py", "makemigrations"]
CMD ["python", "./Student/manage.py", "migrate"]
CMD ["python", "./Student/manage.py", "runserver", "0.0.0.0:8000"]
