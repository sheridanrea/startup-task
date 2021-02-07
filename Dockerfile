# get latest postgres image
FROM postgres:latest
WORKDIR /code
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=supersecret
ENV POSTGRES_DB=postgres
EXPOSE 5432

# install Python 3
RUN apt-get update && apt-get install -y python3 python3-pip

# install dev packages - needed for psycopg2
RUN apt-get -y install python3.7-dev
RUN apt-get -y install postgresql-server-dev-10 gcc python3-dev musl-dev

# install psycopg2 library for python-postgres interactions
RUN pip3 install psycopg2

# Create database with data
RUN python3 set_up.py

# Define api fxs
RUN python3 api.py

