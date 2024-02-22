FROM python:3.11.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

ARG SUPERUSER_USERNAME
ARG SUPERUSER_PASSWORD
ARG SUPERUSER_EMAIL


ENV DJANGO_SUPERUSER_USERNAME=$SUPERUSER_USERNAME \
    DJANGO_SUPERUSER_PASSWORD=$SUPERUSER_PASSWORD \
    DJANGO_SUPERUSER_EMAIL=$SUPERUSER_EMAIL


RUN python manage.py createsuperuser --noinput

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
