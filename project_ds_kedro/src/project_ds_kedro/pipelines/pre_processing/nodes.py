"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.0
"""

import pandas as pd

def df_lisboa(df):
    
    """ This function serves to limit the dataset only to the Territory = Lisboa """
    
    df = df.loc[df['territoryName'] == 'Lisboa']
    return df

def preprocess_time(df):
    """ This function convert time column from object to datetime format."""
    
    # Convert time column 
    df['time'] = pd.to_datetime(df['time']).astype(int)
    
    return df

def func_drop_columns(df):
    """ This function clears the dataframe. Study performed from the heatmap, considering correlation > 0.9 """    
   
    #Remove columns with correlation less than 0.9
    df = df.drop(columns=['territoryName', 'numParishes'])
    
    return df