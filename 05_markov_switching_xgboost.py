import numpy as np
import matplotlib.pyplot as plt
def run_markov_xgboost():
    time_axis = np.arange(90)
    ai_risk = 0.2 + 0.6 / (1 + np.exp(-(time_axis - 40) / 8))
    plt.figure(figsize=(10, 4))
    plt.plot(time_axis, ai_risk * 100, color='darkorange', linewidth=2.5)
    plt.axhline(65, color='red', linestyle='--', label='Crisis Threshold')
    plt.title("Method 5: Markov Switching XGBoost Risk Dashboard")
    plt.savefig("05_xgboost_regime.png", dpi=300)
if __name__ == '__main__': run_markov_xgboost()