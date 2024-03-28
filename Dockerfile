# Container image that runs your code
FROM python:3.12.2

WORKDIR /app

COPY ./requirements.txt .
RUN python -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY test.py /app/test.py

# Code file to execute when the docker container starts up (`entrypoint.sh`)
CMD ["python", "test.py"]