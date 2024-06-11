# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:34:45 2024

@author: User
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 假設 df 是一個包含 OHLC 資料的 DataFrame，並且已經按照日期排序
df = pd.read_csv('data_6414.csv') # Example of loading data
# df should have columns: 'Date', 'Open', 'High', 'Low', 'Close'

def calculate_pivots(df, length):
    df['PivotHigh'] = df['High'].rolling(window=length, center=True).max()
    df['PivotLow'] = df['Low'].rolling(window=length, center=True).min()
    return df

def plot_fibonacci_levels(df, length, show_zero_and_half):
    df = calculate_pivots(df, length)

    # 找到最新的 Pivot High 和 Pivot Low
    last_pivot_high = df['PivotHigh'].dropna().iloc[-1]
    last_pivot_low = df['PivotLow'].dropna().iloc[-1]

    highest_since_last_pivot_low = df.loc[df['PivotLow'].dropna().index[-1]:]['High'].max()
    lowest_since_last_pivot_high = df.loc[df['PivotHigh'].dropna().index[-1]:]['Low'].min()

    # 計算 Fibonacci levels
    fib_0_618 = highest_since_last_pivot_low - (highest_since_last_pivot_low - last_pivot_low) * 0.618
    fib_0_5 = highest_since_last_pivot_low - (highest_since_last_pivot_low - last_pivot_low) * 0.5
    fib_0_382 = highest_since_last_pivot_low - (highest_since_last_pivot_low - last_pivot_low) * 0.382 if show_zero_and_half else None

    # Plotting
    plt.figure(figsize=(14, 7))
    plt.plot(df['Date'], df['Close'], label='Close Price')
    
    plt.axhline(fib_0_618, color='orange', linestyle='--', label='GP 0.618')
    plt.axhline(fib_0_5, color='yellow', linestyle='--', label='GP 0.5')
    
    if show_zero_and_half:
        plt.axhline(fib_0_382, color='green', linestyle='--', label='GP 0.382')

    # 填充區域
    plt.fill_between(df['Date'], fib_0_5, fib_0_618, color='yellow', alpha=0.3)
    if show_zero_and_half:
        plt.fill_between(df['Date'], fib_0_382, fib_0_5, color='green', alpha=0.3)

    # 標記 Pivot Points
    plt.scatter(df['Date'], df['PivotHigh'], color='black', marker='v', label='Pivot High')
    plt.scatter(df['Date'], df['PivotLow'], color='black', marker='^', label='Pivot Low')

    plt.legend()
    plt.title('Auto Fibonacci Golden Pocket')
    plt.show()
    
df = plot_fibonacci_levels(df, length=5, show_zero_and_half=True)
print(df.head())


# 示例使用
# df = pd.read_csv('your_data.csv', parse_dates=['Date'])
# plot_fibonacci_levels(df, length=50, show_zero_and_half=True)
