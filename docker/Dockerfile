FROM python:3.10.6

RUN apt-get update

WORKDIR /PokeApi

COPY . .
COPY requirements.txt ./
RUN pip install -r requirements.txt
#pandas==2.0.1 minio==6.0.2 requests==2.31.0

# ENTRYPOINT echo $PWD & ls -la 

ENTRYPOINT ["tail", "-f", "/dev/null"]


# CMD ["python3", "main.py"]