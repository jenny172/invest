# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 14:07:19 2024

@author: User
"""
import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('data.csv') # Example of loading data

#清理資料
#我們需要成交股數、開盤價、最高價、最低價、收盤價的資料
#並使用Date當作我們的索引值
 
#df.index = pd.to_datetime(df['Date'])
#df = df[['成交股數','開盤價','最高價','最低價','收盤價']]
#df.columns = ['Volume','Open','High','Low','Close']
#df['Close'] = pd.to_numeric(df['Close'])



#我們分別計算5天,10天與20天的移動平均線
df['MA_5'] = df['Close'].rolling(5).mean()
df['MA_10'] = df['Close'].rolling(10).mean()
df['MA_20'] = df['Close'].rolling(20).mean()

# 計算移動平均線
#df['MA'] = df['Close'].rolling(window=ma_length).mean()


#上漲時，fib_0_5 到 fib_0_618的區間
if (df['Date'][last_pivot_high]-df['Date'][last_pivot_low]) > 0 :
    df['MA'] = df['Close'].rolling(window=ma_length).mean()
    ma_in_fib_range = (df['MA'] >= fib_0_5) & (df['MA'] <= fib_0_618)
    return ma_in_fib_range
print("MA in Fibonacci 0.5 to 0.618 range:\n", df[ma_in_fib_range])


#下降時，fib_0_382 到 fib_0_5的區間
if (df['Date'][last_pivot_high]-df['Date'][last_pivot_low]) < 0 :
    df['MA'] = df['Close'].rolling(window=ma_length).mean()
    ma_in_fib_range = (df['MA'] >= fib_0_382) & (df['MA'] <= fib_0_5)
    return ma_in_fib_range
print("MA in Fibonacci 0.382 to 0.5 range:\n", df[ma_in_fib_range])


#下降時，fib_0_5 到 fib_0_618的區間
if (df['Date'][last_pivot_high]-df['Date'][last_pivot_low]) < 0 :
    df['MA'] = df['Close'].rolling(window=ma_length).mean()
    ma_in_fib_range = (df['MA'] >= fib_0_5) & (df['MA'] <= fib_0_618)
    return ma_in_fib_range
print("MA in Fibonacci 0.5 to 0.618 range:\n", df[ma_in_fib_range])