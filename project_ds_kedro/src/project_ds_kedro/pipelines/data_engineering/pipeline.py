"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.0
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import enconde_party
from .nodes import func_remove_outliers_IQR_approach



def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = enconde_party,
            inputs = "pp_election",
            outputs = [
                "encode_party_dataset",
                "label_encoder_party"
            ],
            name = "enconde_party"
        )
        , node(
            func = func_remove_outliers_IQR_approach,
            inputs = "encode_party_dataset",
            outputs = "election_without_outliers_dataset", 
            name = "election_without_outliers_dataset"
        ) 
    ])
