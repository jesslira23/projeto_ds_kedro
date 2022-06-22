"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.0
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preprocess_time

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = preprocess_time,
            inputs = 'election_databse',
            outputs = 'pp_election',
            name  = 'preprocess_election'
        )


    ])
