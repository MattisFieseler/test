# Container image that runs your code
FROM python:3.12.2

WORKDIR /app

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY test.py /app/test.py

# Code file to execute when the docker container starts up (`entrypoint.sh`)
CMD ["python", "test.py"]