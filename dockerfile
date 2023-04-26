FROM python:3.10.6

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt /places/
RUN pip install -r requirements.txt

COPY entrypoint.sh /Carpeta personal/Documentos/Hackwomen-Team-5-Back/entrypoint.sh/

WORKDIR /places
COPY . /places/

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
