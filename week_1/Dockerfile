FROM python:3.9

RUN pip install pandas

WORKDIR /app
COPY pipeline.py pipeline.py

#ENTRYPOINT [ "bash" ] - to run bash on container run
ENTRYPOINT ["python", "pipeline.py"]