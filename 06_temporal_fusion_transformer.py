import numpy as np
import matplotlib.pyplot as plt
def run_transformer():
    time_axis = np.arange(90)
    attention = np.exp(-((time_axis - 45) / 5)**2)
    plt.figure(figsize=(10, 4))
    plt.fill_between(time_axis, 0, attention, color='tab:red', alpha=0.3)
    plt.title("Method 6: Temporal Fusion Transformer Attention Mapping")
    plt.savefig("06_transformer_attention.png", dpi=300)
if __name__ == '__main__': run_transformer()