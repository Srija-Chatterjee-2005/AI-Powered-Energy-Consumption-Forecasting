import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor

def train_model(df):
    # features & target
    X = df[['hour', 'day', 'month', 'weekend']]
    y = df['Energy']

    # split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # model
    model = MLPRegressor(
        hidden_layer_sizes=(64, 64),
        max_iter=300,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model, X_test, y_test