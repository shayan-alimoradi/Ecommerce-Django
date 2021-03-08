
FROM python:3.8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python3","manage.py","migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]