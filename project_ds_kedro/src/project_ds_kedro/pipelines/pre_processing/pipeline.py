"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.0
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import df_lisboa
from .nodes import preprocess_time
from .nodes import func_drop_columns

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = df_lisboa,
            inputs = 'election_databse',
            outputs = 'lisboa_dataset',
            name  = 'lisboa_dataset'
        )
        , node(
            func = preprocess_time,
            inputs = 'lisboa_dataset',
            outputs = 'pp_election_time_correction',
            name  = 'pp_election_time_correction'
        )
        , node(
            func = func_drop_columns,
            inputs = 'pp_election_time_correction',
            outputs = 'pp_election',
            name  = 'preprocess_election'
        )

    ])
