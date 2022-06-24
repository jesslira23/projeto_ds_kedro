"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline
from project_ds_kedro.pipelines import pre_processing as pp
from project_ds_kedro.pipelines import data_engineering as de


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    pre_processing_pipeline = pp.create_pipeline()
    data_engineering_pipeline = de.create_pipeline()


    return {
        "pp": pre_processing_pipeline,
        "de": data_engineering_pipeline,
        "__default__": pre_processing_pipeline}
