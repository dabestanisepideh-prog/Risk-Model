import numpy as np
import matplotlib.pyplot as plt
def run_merton_jump_diffusion(days=90, n_simulations=5000, current_fx=600000, current_coffee=2.42):
    np.random.seed(42)
    dt = 1 / 365
    mu_fx, vol_fx = 0.15, 0.22
    mu_coffee, vol_coffee = 0.05, 0.28
    lambda_fx, jump_mu_fx, jump_vol_fx = 4.0, 0.12, 0.08
    fx_paths = np.zeros((days, n_simulations)) + current_fx
    coffee_paths = np.zeros((days, n_simulations)) + current_coffee
    for t in range(1, days):
        z_fx = np.random.normal(0, 1, n_simulations)
        n_jumps_fx = np.random.poisson(lambda_fx * dt, n_simulations)
        jump_factor_fx = np.zeros(n_simulations)
        for i in range(n_simulations):
            if n_jumps_fx[i] > 0: jump_factor_fx[i] = np.sum(np.random.normal(jump_mu_fx, jump_vol_fx, n_jumps_fx[i]))
        fx_paths[t] = fx_paths[t-1] * np.exp((mu_fx - 0.5 * vol_fx**2) * dt + vol_fx * np.sqrt(dt) * z_fx + jump_factor_fx)
    plt.figure(figsize=(10, 5))
    plt.plot(fx_paths[:, :50], alpha=0.2, color='#2ca02c')
    plt.title("Merton Jump-Diffusion: USD/IRR Stressed Paths (Sharp Jumps)")
    plt.savefig("04_merton_jumps.png", dpi=300)
    print("Method 4 executed successfully.")
if __name__ == '__main__': run_merton_jump_diffusion()