FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install -y python3-dev default-libmysqlclient-dev
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install mysqlclient
ADD . /code/
