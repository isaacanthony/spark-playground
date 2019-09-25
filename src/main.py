"""Entrypoint for pipelines"""
from datetime import datetime
from pyspark.sql import SparkSession
from src.helpers.dataframe import read_csv
from src.pipelines.train import fit as train
from sys import argv


def main() -> None:
    """Entrypoint for pipelines"""
    pipeline = argv[1] if len(argv) > 1 else 'all'

    spark = SparkSession.builder \
        .master('local') \
        .appName('spark-pipeline') \
        .getOrCreate()

    if pipeline in ['all', 'train']:
        dframe = read_csv(spark, 'data/raw/iris.csv')
        model = train(dframe)
        model.save(f"data/interim/model {datetime.now()}")

    if pipeline in ['all', 'test']:
        None


def healthy() -> None:
    """Placeholder health check"""
    return True


if __name__ == '__main__':
    main()
