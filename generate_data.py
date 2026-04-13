import pandas as pd
import numpy as np

# 30 days hourly data
date_range = pd.date_range(start="2023-01-01", periods=24*30, freq="h")

df = pd.DataFrame()
df["Datetime"] = date_range

# Time features
df["hour"] = df["Datetime"].dt.hour
df["day"] = df["Datetime"].dt.dayofweek
df["month"] = df["Datetime"].dt.month

# Weekend
df["weekend"] = df["day"].apply(lambda x: 1 if x >= 5 else 0)

np.random.seed(42)

# Patterns
base = 100
hour_effect = df["hour"].apply(lambda x: 30 if 6 <= x <= 10 else (50 if 17 <= x <= 22 else 10))
weekend_effect = df["weekend"].apply(lambda x: -20 if x == 1 else 0)
season_effect = 20  # constant since only 1 month

noise = np.random.randint(-10, 10, len(df))

df["Energy"] = base + hour_effect + weekend_effect + season_effect + noise

df = df[["Datetime", "Energy"]]

df.to_csv("data/energy.csv", index=False)

print("✅ Small energy.csv generated!")