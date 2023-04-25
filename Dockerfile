# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.11-slim

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY entrypoint.sh  /Users/familiamoctezuma/Documents/GitHub/drf_2/entrypoint.sh

#Required in MAC OS to run the entrypoint .sh script
RUN  sed -i 's/\r$//' /Users/familiamoctezuma/Documents/GitHub/Hackwomen-Team-5-Back/entrypoint.sh \
        && chmod 744 /Users/familiamoctezuma/Documents/GitHub/Hackwomen-Team-5-Back/entrypoint.sh


WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
ENTRYPOINT [ "/Users/familiamoctezuma/Documents/GitHub/Hackwomen-Team-5-Back/entrypoint.sh"]
CMD ["gunicorn", "core.wsgi"]

