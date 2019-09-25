"""Training pipeline"""
from pyspark.ml import Pipeline, PipelineModel
from pyspark.sql import DataFrame


def fit(dframe: DataFrame) -> PipelineModel:
    """Fit on training data"""
    pipeline = Pipeline(stages=[])
    return pipeline.fit(dframe)
