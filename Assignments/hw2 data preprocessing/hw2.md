# Assignment 2: Data Preprocessing

## Question 1: Primary benefit of detrending a time series

The primary benefit of detrending a time series is to remove the long-term trend component, which can reveal underlying patterns and make the series stationary. This process offers several advantages:

1. Stationarity: Detrending helps achieve stationarity, a key assumption for many time series analysis techniques.

2. Revealing hidden patterns: By removing the trend, seasonal patterns and cyclical fluctuations become more apparent.

3. Improved forecasting: Detrended data often leads to more accurate short-term forecasts.

4. Easier interpretation: Without the dominating trend, it's easier to interpret the effects of other factors on the time series.

5. Facilitates comparison: Detrending allows for better comparison between different time series by removing the influence of their individual trends.

6. Enhanced statistical analysis: Many statistical tests and models assume stationarity, which detrending helps achieve.

In summary, detrending is crucial for uncovering the true underlying dynamics of a time series, enabling more accurate analysis and forecasting.

## Question 2: Outline the key advantages of removing the seasonal component from a time series prior to processing or forecasting.

Removing the seasonal component from a time series prior to processing or forecasting offers several key advantages:

1. Stationarity: Seasonal components can introduce non-stationarity, which can complicate analysis and forecasting. Removing the seasonal component helps achieve stationarity.

2. Revealing underlying patterns: By isolating the seasonal component, it becomes easier to understand and model its behavior.

3. Improved forecasting: Detrended data often leads to more accurate short-term forecasts.

4. Easier interpretation: Without the seasonal component, it's easier to interpret the effects of other factors on the time series.

5. Facilitates comparison: Detrending allows for better comparison between different time series by removing the influence of their individual trends.

6. Enhanced statistical analysis: Many statistical tests and models assume stationarity, which detrending helps achieve.

In summary, removing the seasonal component from a time series prior to processing or forecasting can lead to more accurate and reliable analysis and forecasting.


## Question 3: Time Series Analysis and Seasonal Adjustment

Consider a time series X = {X₁, X₂, ...} defined by the following recursion:

Xₖ = α cos(2πk/T) + β sin(2πk/T) + φXₖ₋₁ + ϵₖ + θϵₖ₋₁

where ϵₖ ~ iid N(0, σ²).

Answer the following questions:

a) Write a Python script to generate and plot a sample path of length L = 1000 using the following parameters:
   - α = 2
   - β = 0.5
   - T = 50
   - φ = 0.9
   - θ = 0.7
   - σ² = 1
   - X₀ = 0

```python
import numpy as np
import matplotlib.pyplot as plt

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
time_series = np.zeros(L)
time_series[0] = X_0        

for k in range(1, L):
    time_series[k] = alpha * np.cos(2 * np.pi * k / T) + beta * np.sin(2 * np.pi * k / T) + phi * time_series[k-1] + theta * time_series[k-1] + np.random.normal(0, sigma_sq)

# Plot the time series
plt.figure(figsize=(10, 6))
plt.plot(time_series)
plt.title('Time Series')    
plt.show()
``` 



b) Plot the autocorrelation function (ACF) of the generated sample path.

```python   
from statsmodels.tsa.seasonal import STL

# Perform STL decomposition
stl = STL(time_series, period=T)
result = stl.fit()

# Plot the original time series, trend, seasonal, and residual components
plt.figure(figsize=(12, 8))                 
plt.subplot(411)
plt.plot(time_series)
plt.title('Original Time Series')
plt.subplot(412)
plt.plot(result.trend)
plt.title('Trend Component')
plt.subplot(413)
plt.plot(result.seasonal)   
plt.title('Seasonal Component')
plt.subplot(414)
plt.plot(result.resid)
plt.title('Residual Component')
plt.tight_layout()
plt.show()
```         

c) Perform a seasonal adjustment of the sample path generated in the previous step using the STL (Seasonal and Trend decomposition using Loess) method. Ensure that the seasonal component being removed is strictly periodic (e.g., compute the average of all seasons). Plot the residual signal after the seasonal adjustment.

```python
# Calculate the average seasonal component
seasonal_component = np.mean(result.seasonal, axis=1)

# Subtract the seasonal component from the original time series
adjusted_series = time_series - seasonal_component

# Plot the residual signal after seasonal adjustment
plt.figure(figsize=(10, 6))
plt.plot(adjusted_series)
plt.title('Residual Signal After Seasonal Adjustment')
plt.show()
``` 

d) Plot the ACF of the residuals.

```python
# Plot the ACF of the residuals
plt.figure(figsize=(10, 6))
plt.acorr(adjusted_series, maxlags=50)
plt.title('ACF of Residuals After Seasonal Adjustment')
plt.show()
```

e) Does the seasonal adjustment aid in the visual analysis of the ACF? Justify your answer.

The seasonal adjustment aids in the visual analysis of the ACF by removing the strong seasonal component, making the ACF more interpretable.    


