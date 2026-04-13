import os
import joblib
import numpy as np
import pandas as pd
from datetime import datetime

from src.data_preprocessing import load_data, preprocess
from src.feature_engineering import create_features
from src.model_training import train_model
from src.evaluation import evaluate
from src.visualization import plot_all

# ---------------- CONFIG ----------------
RANDOM_STATE = 42

os.makedirs("models", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

# ---------------- PIPELINE ----------------
def main():
    try:
        log("📥 Loading dataset...")
        df = load_data("data/energy.csv")

        log("🧹 Preprocessing data...")
        df = preprocess(df)

        log("⚙️ Feature engineering...")
        df = create_features(df)

        log("🤖 Training model...")
        model, X_test, y_test = train_model(df)

        log("📊 Making predictions...")
        preds = model.predict(X_test)

        log("📏 Evaluating model...")
        rmse, r2, mae = evaluate(y_test, preds)

        # ---------------- SAVE MODEL ----------------
        joblib.dump(model, "models/energy_model.pkl")

        # ---------------- SAVE METRICS ----------------
        with open("outputs/metrics.txt", "w") as f:
            f.write(f"RMSE: {rmse}\n")
            f.write(f"R2: {r2}\n")
            f.write(f"MAE: {mae}\n")

        # ---------------- VISUALIZATION ----------------
        plot_all(df, y_test, preds)

        log("✅ Training complete. Model saved successfully.")

    except Exception as e:
        log(f"❌ Error occurred: {e}")

if __name__ == "__main__":
    main()