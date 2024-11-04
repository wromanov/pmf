# 1.2.Obtenção via bibliotecas/APIs
# Obter Dados Yahoo Finance via biblioteca "yfinance"

import yfinance as yf

import matplotlib.pyplot as plt

#itub4 = yf.download('ITUB4.SA', start='2024-01-01')

itub4 = yf.download('ITUB4.SA', period='max')

print(itub4.head())

print(itub4.Close.max())

print(itub4.Close.min())

print(itub4.Close.pct_change())
itub4.Close.plot()
plt.show()

