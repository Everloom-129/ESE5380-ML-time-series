'''
# Question 3: Time Series Analysis and Seasonal Adjustment
Tony Wang

Consider a time series X = {X₁, X₂, ...} defined by the following recursion:

# Xₖ = α cos(2πk/T) + β sin(2πk/T) + φXₖ₋₁ + ϵₖ + θϵₖ₋₁

# where ϵₖ ~ iid N(0, σ²).

# Answer the following questions:
'''
# a) Write a Python script to generate and plot a sample path of length L = 1000 using the following parameters:
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.seasonal import STL

# set random seed as 538
np.random.seed(538)
# Define the parameters
alpha = 2
beta = 0.5
T = 50
phi = 0.9
theta = 0.7
sigma_sq = 1
X_0 = 0

# Generate the time series
L = 1000
X = np.zeros(L)
X[0] = X_0        
epsilon = np.random.normal(0, np.sqrt(sigma_sq), L)

for k in range(1, L):
    X[k] = alpha * np.cos(2 * np.pi * k / T) + beta * np.sin(2 * np.pi * k / T) \
    + phi * X[k-1] + epsilon[k] + theta * epsilon[k-1]

# Plot the time series
plt.figure(figsize=(12, 6))
plt.plot(X, label='Time Series')
plt.title('Original Time Series')       
plt.xlabel('Time')  
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.savefig('T2_a.png')
plt.close()

# b) Plot the autocorrelation function (ACF) of the generated sample path.
plt.figure(figsize=(12, 6))
plot_acf(X, lags=50, ax=plt.gca()) # current axis
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.title('ACF of Given Time Series')
plt.grid(True)
plt.savefig('T2_b.png')
plt.close()

# c) Perform a seasonal adjustment of the sample path generated in the previous step using the STL (Seasonal and Trend decomposition using Loess) method. Ensure that the seasonal component being removed is strictly periodic (e.g., compute the average of all seasons). Plot the residual signal after the seasonal adjustment.

# Custom STL, the average seasonal component
# seasonal_component = np.tile(np.mean(X.reshape(-1, T), axis=0), L // T + 1)[:L]
# adjusted_series = X - seasonal_component

# Standard STL decomposition on the time series
stl = STL(X, period=T)
result = stl.fit()

# Extract the residual component
residuals = result.resid

plt.figure(figsize=(12, 6))
plt.plot(residuals, label='Residual Signal')
plt.title('Residual Signal After Seasonal Adjustment')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.savefig('T2_c.png')
plt.close()

# d) Plot the ACF of the residuals.
plt.figure(figsize=(12, 6))
plot_acf(residuals, lags=50, ax=plt.gca()) 
plt.title('ACF of Residuals After Seasonal Adjustment')
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.grid(True)
plt.savefig('T2_d.png')
plt.close()