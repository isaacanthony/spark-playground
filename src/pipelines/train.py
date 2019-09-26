"""Training pipeline"""
from pyspark.ml import Pipeline, PipelineModel
from pyspark.sql import DataFrame
from src.transformers.custom_normalizer import CustomNormalizer
# from pyspark.ml.feature import Normalizer

def fit(dframe: DataFrame) -> PipelineModel:
    """Fit on training data"""
    pipeline = Pipeline(stages=[
        CustomNormalizer(),
    ])

    return pipeline.fit(dframe)
