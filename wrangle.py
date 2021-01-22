import pandas as pd
import numpy as np

def wrangle_insects():
    insects = pd.read_csv('insects.csv')
    insects = insects.set_index('#')
    insects = insects.drop(columns=['Icon Filename', 'Critterpedia Filename', 'Furniture Filename', 'Internal ID', 'Unique Entry ID'])
    insects = insects.fillna(0)
    insects['Spawn Rates'] = insects['Spawn Rates'].where(insects['Spawn Rates'] != '5–10', 8).astype(int)
    return insects