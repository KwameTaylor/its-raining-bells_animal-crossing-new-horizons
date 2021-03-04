import pandas as pd
import numpy as np

def wrangle_insects():
    # read from csv file
    insects = pd.read_csv('insects.csv')
    # set the index to #
    insects = insects.set_index('#')
    # drop columns I won't be using
    insects = insects.drop(columns=['Icon Filename', 'Critterpedia Filename', 'Furniture Filename', 'Internal ID', 'Unique Entry ID'])

    # convert Spawn Rates to an integer and handle range value (brute force method for now)
    # Because one of the values is a range, I'm going to make it the average of
    # the start and end values rounded to the nearest integer, which is 8.
    insects['Spawn Rates'] = insects['Spawn Rates'].where(insects['Spawn Rates'] != '5–10', 8).astype(int)

    # impute NaNs with 0s for now
    insects = insects.fillna(0)

    assert insects.isna().sum().sum() == 0, "There are unhandled nulls in the DataFrame."
    # will raise an AssertionError exception if there are any nulls that were unsuccessfully handled

    return insects