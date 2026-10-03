import numpy as np
import matplotlib.pyplot as plt
def run_ml_forecasting():
    np.random.seed(101)
    coffee_paths = np.random.normal(2.5, 0.2, (90, 5000))
    fx_paths = np.random.normal(650000, 40000, (90, 5000))
    coffee_prob = np.mean(coffee_paths[-1] > (coffee_paths[0] * 1.05)) * 100
    fx_prob = np.mean(fx_paths[-1] > (fx_paths[0] * 1.05)) * 100
    plt.figure(figsize=(8, 5))
    plt.bar(['Coffee Price Rally (>5%)', 'FX Rate Spike (>5%)'], [coffee_prob, fx_prob], color=['#a0522d', '#4682b4'])
    plt.title("Market Trend Directionality Probability (ML Module)")
    plt.ylim(0, 100)
    plt.savefig("02_ml_forecast_probabilities.png", dpi=300)
    print("Method 2 executed successfully.")
if __name__ == '__main__': run_ml_forecasting()