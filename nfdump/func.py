# import pandas as pd
from os.path import isfile, join
from os import listdir


def max_count(df):
    return df.count().max()


# def timestamp2datetime(series):
# return pd.to_datetime(series, unit='s', errors='coerce')


def list_files(folder):
    """
        Read the names of all the raw_input in the input folder
    :return: An array with the names of all the files of a folder
    """
    return [f for f in listdir(folder) if isfile(join(folder, f))]

# NAT increases the availability of public IP addresses as well as IPv6 does
