import numpy as np
import matplotlib.pyplot as plt
def run_optimization(order_volume=50000):
    np.random.seed(101)
    coffee_final = np.random.normal(2.45, 0.15, 10000)
    fx_final_baseline = np.random.normal(620000, 30000, 10000)
    fx_final_stressed = fx_final_baseline * 1.50
    costs_baseline = (coffee_final * fx_final_baseline * order_volume) / 1e9
    costs_stressed = (coffee_final * fx_final_stressed * order_volume) / 1e9
    var_baseline = np.percentile(costs_baseline, 95)
    var_stressed = np.percentile(costs_stressed, 95)
    plt.figure(figsize=(12, 6))
    plt.hist(costs_baseline, bins=60, alpha=0.6, color='teal', label='Baseline Scenario')
    plt.hist(costs_stressed, bins=60, alpha=0.5, color='crimson', label='Stressed Scenario (50% FX Shock)')
    plt.axvline(var_baseline, color='darkslategrey', linestyle='--', label=f'Baseline VaR 95% ({var_baseline:.2f}B)')
    plt.axvline(var_stressed, color='red', linestyle='--', label=f'Stressed VaR 95% ({var_stressed:.2f}B)')
    plt.title("Risk Optimization & Procurement Stress Test Analysis")
    plt.xlabel("Total Procurement Cost (Billion IRR)")
    plt.legend()
    plt.savefig("03_risk_optimization_analysis.png", dpi=300)
    print("Method 3 executed successfully.")
if __name__ == '__main__': run_optimization()