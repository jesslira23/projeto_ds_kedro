"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.0
"""

import pandas as pd


def preprocess_time(df: pd.DataFrame):
    """ This function convert time column from object to datetime format."""
    
    # Convert time column 
    df['time'] = pd.to_datetime(df['time'])
    
    return df