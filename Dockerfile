FROM jupyter/pyspark-notebook:latest
COPY src/requirements.txt requirements.txt
RUN pip install -r requirements.txt
