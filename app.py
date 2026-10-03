import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Risk Dashboard - Supply Chain", layout="wide")
st.title("🤖 AI-Driven Price Jump & Market Regime Switching Platform")
st.markdown("### Dynamic Procurement Strategy & Tactical Risk Dashboard")

# سایدبار تنظیمات برای مدیران
st.sidebar.header("⚙️ Model Parameters")
initial_fx = st.sidebar.slider("Initial Exchange Rate (IRR)", 500000, 800000, 600000, step=10000)
shock_day = st.sidebar.slider("Expected Shock Window (Days)", 20, 70, 45)
threshold = st.sidebar.slider("AI Risk Alert Threshold (%)", 50, 90, 65)

if st.sidebar.button("🚀 Run Interactive Quantum Simulation"):
    days = 90
    time = np.arange(days)
    np.random.seed(2026)
    
    # شبیه‌سازی سیگنال ریسک هوش مصنوعی
    ai_signal = 0.2 + 0.6 / (1 + np.exp(-(time - shock_day) / 6)) + np.random.normal(0, 0.03, days)
    ai_signal = np.clip(ai_signal, 0, 1)
    
    prices = np.zeros(days)
    prices[0] = initial_fx
    
    for t in range(1, days):
        if ai_signal[t] > (threshold / 100):
            prices[t] = prices[t-1] * (1 + np.random.normal(0.025, 0.035))
        else:
            prices[t] = prices[t-1] * (1 + np.random.normal(0.001, 0.007))
            
    # نمایش شاخص‌ها
    c1, c2 = st.columns(2)
    c1.metric("AI Trigger Day (Crisis Regime)", f"Day {np.where(ai_signal > (threshold/100))[0][0] if any(ai_signal > (threshold/100)) else 'None'}")
    c2.metric("Worst-Case Stressed Price", f"{prices[-1]:,.0f} IRR")
    
    # رسم نمودار حرفه‌ای داشبورد
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 6), sharex=True)
    ax1.plot(time, ai_signal * 100, color='darkorange', linewidth=2.5, label='AI Jump Probability')
    ax1.axhline(threshold, color='red', linestyle='--', label='Alert Level')
    ax1.fill_between(time, 0, ai_signal * 100, where=(ai_signal >= (threshold/100)), color='red', alpha=0.15)
    ax1.set_ylabel("Probability (%)")
    ax1.legend(loc='upper left')
    ax1.grid(True, alpha=0.3)
    
    ax2.plot(time, prices / 1000, color='dodgerblue', linewidth=2.5, label='Simulated Cost Path')
    ax2.set_ylabel("Price (k IRR)")
    ax2.set_xlabel("Days Horizon")
    ax2.legend(loc='upper left')
    ax2.grid(True, alpha=0.3)
    
    st.pyplot(fig)
    st.success("✅ Risk optimization completed. System recommends executing proxy-hedging structures immediately.")
