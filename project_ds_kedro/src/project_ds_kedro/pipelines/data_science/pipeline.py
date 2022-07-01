"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.0
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import func_split_data
from .nodes import func_fit_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = func_split_data,
            inputs = "election_without_outliers_dataset",
            outputs = ['X_train', 'X_test', 'y_train', 'y_test'], 
            name = "split_data"
        ) 
        , node(
            func = func_fit_model,
            inputs = ['X_train', 'X_test', 'y_train', 'y_test'],
            outputs = "regression_model",
            name = "fit_model"
        )
    ])
