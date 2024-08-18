FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY ./django_deployment /code/app

EXPOSE 8000:8000

CMD ["python3", "manage.py", "runserver"]
