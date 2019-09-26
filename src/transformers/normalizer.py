"""Normalize all numeric columns"""
from pyspark.ml import Transformer
from pyspark.ml.feature import Normalizer as DefaultNormalizer
from pyspark.ml.util import DefaultParamsReadable, DefaultParamsWritable
from pyspark.sql import DataFrame


COLS = [
    'sepal_length',
    'sepal_length',
    'sepal_width',
    'petal_length',
    'petal_width',
]


class Normalizer(Transformer, DefaultParamsReadable, DefaultParamsWritable):
    """Normalizes all numeric features"""


    def _transform(self, dframe: DataFrame) -> DataFrame:
        for col in COLS:
            scaler = DefaultNormalizer(
                inputCol=col,
                outputCol='scaled_' + col,
                p=1.0,
            )

            dframe = scaler.transform(dframe)

        print(dframe.head(5))
        return dframe
