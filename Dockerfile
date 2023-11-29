FROM python:3.9
RUN mkdir -p /Student
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /Student
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean
RUN pip install --upgrade pip
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python","./Student/manage.py", "runserver", "0.0.0.0:8000"]
