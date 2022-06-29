"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.0
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import scipy.stats as stats


def enconde_territory_name(df):
    
    """This function converts the territoryName column to numeric categories"""

    label_encoder = LabelEncoder()
    label_encoder = label_encoder.fit(df['territoryName'])
    df['territoryName'] = label_encoder.transform(df['territoryName'])

    return df, label_encoder


def enconde_party(df):
    
    """This function converts the Party column to numeric categories"""

    label_encoder_party = LabelEncoder()
    label_encoder_party = label_encoder_party.fit(df['Party'])
    df['Party'] = label_encoder_party.transform(df['Party'])

    return df, label_encoder_party


def func_normalized_dataset(df):
    """This function is intended to normalize the data"""

    cols_normalizado = ['territoryName','totalMandates', 'numParishes', 'numParishesApproved', 'blankVotes', 'nullVotes', 'subscribedVoters', 'totalVoters', 'pre.blankVotes', 'pre.nullVotes', 'pre.subscribedVoters', 'pre.totalVoters', 'Party', 'Mandates', 'Votes','Hondt', 'FinalMandates']
    norm = MinMaxScaler()

    df[cols_normalizado] = norm.fit_transform(df[cols_normalizado])
    
    return df


def func_remove_outliers_zscore(df):
        """ This function detects and removes outliers using the Z-score method """

        z = stats.zscore(df)
        df = df[(z<3).all(axis = 1)]
        
        return df