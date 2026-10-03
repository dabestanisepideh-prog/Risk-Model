import numpy as np
import matplotlib.pyplot as plt
def run_monte_carlo(days=90, n_simulations=5000, current_coffee=2.42, current_fx=600000):
    np.random.seed(101)
    mu_coffee, vol_coffee = 0.0002, 0.018
    mu_fx, vol_fx = 0.001, 0.012
    correlation = 0.2
    cov_matrix = [[vol_coffee**2, correlation*vol_coffee*vol_fx], [correlation*vol_coffee*vol_fx, vol_fx**2]]
    coffee_paths = np.zeros((days, n_simulations)) + current_coffee
    fx_paths = np.zeros((days, n_simulations)) + current_fx
    for t in range(1, days):
        shocks = np.random.multivariate_normal([0, 0], cov_matrix, n_simulations)
        coffee_paths[t] = coffee_paths[t-1] * np.exp(mu_coffee - 0.5*vol_coffee**2 + shocks[:, 0])
        fx_paths[t] = fx_paths[t-1] * np.exp(mu_fx - 0.5*vol_fx**2 + shocks[:, 1])
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    ax1.plot(fx_paths[:, :100], alpha=0.15, color='#1f77b4')
    ax1.set_title("USD to IRR Exchange Rate Paths")
    ax2.plot(coffee_paths[:, :100], alpha=0.15, color='#ff7f0e')
    ax2.set_title("Global Coffee Price (USD/lb) Paths")
    plt.savefig("01_monte_carlo_paths.png", dpi=300)
    print("Method 1 executed successfully.")
if __name__ == '__main__': run_monte_carlo()