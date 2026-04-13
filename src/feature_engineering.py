def create_features(df):
    df['hour'] = df.index.hour
    df['day'] = df.index.dayofweek
    df['month'] = df.index.month
    df['weekend'] = df['day'].apply(lambda x: 1 if x >= 5 else 0)
    return df