"""Helper script for interacting with dataframes"""
import pandas as pd
from pyspark.sql import DataFrame, SparkSession


def read_csv(spark: SparkSession, file_path: str) -> DataFrame:
    """Converts a CSV into a spark DataFrame"""
    spark.conf.set('spark.sql.execution.arrow.enabled', 'true')
    dframe = pd.read_csv(file_path)
    return spark.createDataFrame(dframe)
