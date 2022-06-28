"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.0
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder



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


def func_remove_outliers(df):
    """ This function detects and removes outliers using the Interquartile range(IQR) method """
    
    #Detection outliers and replace the data points that lie outside of the lower and the upper bound with a NULL value.
    for x in df:
        q75,q25 = np.percentile(df.loc[:,x],[75,25])
        intr_qr = q75-q25
 
        max = q75+(1.5*intr_qr)
        min = q25-(1.5*intr_qr)
 
        df.loc[df[x] < min,x] = np.nan
        df.loc[df[x] > max,x] = np.nan
    
    #Drop the null values 
    df = df.dropna(axis = 0)
    
    return df