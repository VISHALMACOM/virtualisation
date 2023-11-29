# base image
FROM python:3.8.2
# make workdir to the app of DJANGO 
WORKDIR /home/ubuntu/virtualisation/Student
# options
ENV PYTHONUNBUFFERED 1
# update pip
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y netcat-openbsd gcc && \
    apt-get clean
  
RUN pip install --upgrade pip
#RUN pip3 install virtualenv
#RUN virtualenv venv
#ENV PATH="/Student/venv/bin:$PATH"
RUN mkdir static

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#copy host files to images
COPY . .
# create static directory
RUN ls -a

# RUN python manage.py collectstatic --no-input
EXPOSE 8000

CMD ["python","./Student/manage.py", "runserver", "0.0.0.0:8000"]
