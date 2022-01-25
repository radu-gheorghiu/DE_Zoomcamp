FROM python:3.9

RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app
RUN mkdir -p /app/data
COPY data_ingestion.py data_ingestion.py

#ENTRYPOINT [ "bash" ] - to run bash on container run
ENTRYPOINT ["python", "data_ingestion.py"]