FROM jupyter/pyspark-notebook:latest
COPY . /home/jovyan
RUN pip install --no-cache-dir .
