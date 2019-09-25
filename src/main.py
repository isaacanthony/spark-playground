"""Entrypoint for pipelines"""
from pyspark.sql import SparkSession
from src.helpers.dataframes import read_csv


def main() -> None:
    """Entrypoint for pipelines"""
    spark = SparkSession.builder \
        .master('local') \
        .appName('spark-pipeline') \
        .getOrCreate()

    dframe = read_csv(spark, 'data/raw/iris.csv')
    print(dframe.head())


def healthy() -> None:
    """Placeholder health check"""
    return True


if __name__ == '__main__':
    main()
