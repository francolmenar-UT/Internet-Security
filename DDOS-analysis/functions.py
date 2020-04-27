import pandas as pd


def timestamp2datetime(series):
    return pd.to_datetime(series, unit='s', errors='coerce')


def bytes2bits(series):
    try:
        return series * 8
    except AttributeError:
        return series


def max_count(df):
    return df.count().max()


def show_top(*args):
    if len(args) == 1:
        return args[0].head()
    elif len(args) == 2:
        return args[0].head(args[1])


def show_bottom(*args):
    if len(args) == 1:
        return args[0].tail()
    elif len(args) == 2:
        return args[0].tail(args[1])
