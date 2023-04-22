FROM python:3.10.6

WORKDIR /places

COPY requirements.txt /places/
RUN pip install -r requirements.txt

COPY . /places/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
