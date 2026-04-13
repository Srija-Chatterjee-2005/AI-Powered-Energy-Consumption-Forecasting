import matplotlib.pyplot as plt

def plot_all(df, y_true, y_pred):
    plt.figure(figsize=(12, 5))

    # Actual vs Predicted
    plt.plot(y_true.values, label="Actual Energy", linewidth=2)
    plt.plot(y_pred, label="Predicted Energy", linewidth=2)

    plt.title("Energy Consumption: Actual vs Predicted")
    plt.xlabel("Samples")
    plt.ylabel("Energy Usage")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("outputs/prediction_plot.png")

    plt.show()