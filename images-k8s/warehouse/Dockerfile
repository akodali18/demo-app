FROM python:3.9

RUN apt update && apt install git python3-pip -y

# Copy app and setup requirements
COPY warehouse /warehouse
WORKDIR /warehouse

# setup app requirements
RUN pip3 install -r requirements.txt

