"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.0
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import scipy.stats as stats


def enconde_territory_name(df):
    
    """Convertendo a coluna territoryName em categorias de numeros """

    label_encoder = LabelEncoder()
    label_encoder = label_encoder.fit(df['territoryName'])
    df['territoryName'] = label_encoder.transform(df['territoryName'])

    return df, label_encoder

def enconde_party(df):
    
    """Convertendo a coluna territoryName em categorias de numeros """

    label_encoder_party = LabelEncoder()
    label_encoder_party = label_encoder_party.fit(df['Party'])
    df['Party'] = label_encoder_party.transform(df['Party'])

    return df, label_encoder_party


def func_remove_outliers_zscore(df):
        """ This function detects and removes outliers using the Z-score method """

        z = stats.zscore(df)
        df = df[(z<3).all(axis = 1)]
        return df