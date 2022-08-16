FROM python:3.10-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
# RUN python manage.py collectstatic
# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
CMD [ "gunicorn", "composeexample.wsgi:application", "--bind", "0.0.0.0:8000" ]