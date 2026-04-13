import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    if df.empty:
        raise ValueError("CSV is empty")

    df['Datetime'] = pd.to_datetime(df['Datetime'])
    df.set_index('Datetime', inplace=True)

    return df


def preprocess(df):
    # ensure hourly format
    df = df.resample('h').mean()

    # fill missing values
    df = df.ffill()

    return df