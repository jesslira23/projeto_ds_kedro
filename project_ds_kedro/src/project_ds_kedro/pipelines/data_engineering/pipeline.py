"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.0
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import enconde_territory_name
from .nodes import enconde_party



def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = enconde_territory_name,
            inputs = "pp_election",
            outputs = [
                "encode_territoryname_dataset",
                "label_encoder"
            ],
            name = "enconde_territory_name"
        ),
        node(
            func = enconde_party,
            inputs = "encode_territoryname_dataset",
            outputs = [
                "encode_party_dataset",
                "label_encoder_party"
            ],
            name = "enconde_party"
        )
    ])
