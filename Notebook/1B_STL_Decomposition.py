# STL Decomposition: Seasonal-Trend Decomposition using Loess
# Tony Wang
# Oct 2024
## Following the course notes: 1B_Characteristics of Time Series_v7.pdf

### 1. Time Series Decomposition

import numpy as np
import matplotlib . pyplot as plt
from statsmodels . tsa. seasonal import STL
from statsmodels . graphics . tsaplots import plot_acf
from statsmodels . stats . diagnostic import acorr_ljungbox

### 1.1 Generate a Time Series

np.random.seed(0)

time = np.arange(300)

trend = 0.1 * time - 15
seasonal = 10 * np.sin(2 * np.pi * time / 20)

noise = np.random.normal(scale=2, size=len(time))

data = trend + seasonal + noise

#### Plot the Time Series

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 4), sharex=True)
# Plot components in the first subplot
ax1.plot(time, trend, color='red', label='Trend')
ax1.plot(time, seasonal, color='green', label='Seasonality')
ax1.plot(time, noise, color='blue', label='Noise')
ax1.set_ylabel('Value')
ax1.legend()
ax1.set_title('Individual Components')
# Plot combined time series in the second subplot

ax2.plot(time, data, label='Combined Time Series')
ax2.set_xlabel('Time')
ax2.set_ylabel('Value')
ax2.legend()
ax2.set_title('Combined Time Series')

plt.tight_layout()
plt.show()


### 1.2 STL Decomposition

stl = STL(data, period=20)
stl_result = stl.fit()
# Create a plot with three subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(6, 5), sharex=True)
fig.suptitle('STL Decomposition of Time Series', fontsize=16)
# Plot trend component
ax1.plot(time, stl_result.trend, color='red', label='Trend')
ax1.set_ylabel('Value')
ax1.legend(loc='upper left')
# Plot seasonal component
ax2.plot(time, stl_result.seasonal, color='green', label='Seasonal')
ax2.set_ylabel('Value')
ax2.legend(loc='upper left')
# Plot residual component (noise)
ax3.plot(time, stl_result.resid, color='blue', label='Residual')
ax3.set_xlabel('Time')
ax3.set_ylabel('Value')
ax3.legend(loc='upper left')
ax3.set_title('Residuals')
ax3.set_ylim(-10, 10)

plt.tight_layout()
plt.show()

### 1.3 Residual Analysis

residuals = stl_result.resid


