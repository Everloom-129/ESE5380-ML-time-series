import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Download historical stock data (e.g. , for Apple stock ’AAPL ’)
stock_data = yf.download('AAPL', start='2020-01-01', end='2023-01-01')
# Extract adjusted closing prices
prices = stock_data['Adj Close']

plt.figure(figsize=(10, 5))

# Subplot 1: Temporal evolution of AAPL stock prices
plt.subplot(1, 2, 1)
plt.plot(prices, label='Stock Prices', color='blue')
plt.title('Temporal Evolution of AAPL Stock Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(True)
plt.legend()

# Subplot 2: Histogram of AAPL stock prices
plt.subplot(1, 2, 2)
plt.hist(prices, bins=30, color='blue', alpha=0.7)
plt.title('Histogram of Stock Prices (AAPL)')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()



# Compute log returns (log ratio transformation )
log_returns = np.log(prices / prices.shift(1)).dropna()

plt.figure(figsize=(10, 5))

# Subplot 1: Temporal evolution of log returns
plt.subplot(1, 2, 1)
plt.plot(log_returns, label='Log Returns', color='green')
plt.title('Temporal Evolution of AAPL Log Returns')
plt.xlabel('Date')
plt.ylabel('Log Return')
plt.grid(True)
plt.legend()

# Subplot 2: Plot histogram of log returns
plt.subplot(1, 2, 2)
plt.hist(log_returns, bins=30, color='green', alpha=0.7)
plt.title('Histogram of Log Returns (AAPL)')
plt.xlabel('Log Return')
plt.ylabel('Frequency')

# Show the plot
plt.tight_layout()
plt.show()