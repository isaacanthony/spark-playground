"""Training pipeline"""
from pyspark.ml import Pipeline, PipelineModel
from pyspark.sql import DataFrame
from src.transformers.normalizer import Normalizer


def fit(dframe: DataFrame) -> PipelineModel:
    """Fit on training data"""
    pipeline = Pipeline(stages=[
        Normalizer(),
    ])

    return pipeline.fit(dframe)
