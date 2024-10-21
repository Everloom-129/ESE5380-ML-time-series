# FAQ: Time Series as Stochastic Processes

## 1. What is a stochastic process, and how does it relate to time series data?

A stochastic process is a collection of random variables indexed by time. In the context of time series analysis, the observed data points in a time series are considered realizations of these random variables. This statistical perspective allows us to use probabilistic methods to analyze, model, and forecast the behavior of time series data.

For example, a daily record of stock prices can be viewed as a sample path of an underlying stochastic process that governs the stock's price fluctuations.

## 2. What are some important statistical properties of stochastic processes used in time series analysis?

Key properties include:

- **Mean:** The average value of the process at a given time.
- **Variance:** A measure of the process's variability around the mean.
- **Autocovariance:** A measure of how the process correlates with itself over different time lags.
- **Autocorrelation:** A scaled version of autocovariance, ranging between -1 and 1, indicating the strength and direction of the linear relationship between the process and its lagged values.

These properties help us understand the underlying patterns, volatility, and dependencies within a time series.

## 3. What is stationarity, and why is it important in time series analysis?

Stationarity means that the statistical properties of a stochastic process do not change over time. There are two main types:

- **Strong-Sense Stationarity (SSS):** The joint distribution of any collection of random variables from the process is invariant to time shifts.
- **Weak-Sense Stationarity (WSS):** The mean and autocovariance of the process remain constant over time.

Stationarity is crucial for many time series modeling techniques. Assuming stationarity simplifies model development and allows us to make reliable forecasts.

## 4. How can we test for stationarity in time series data?

One widely used test for stationarity is the Augmented Dickey-Fuller (ADF) test. The ADF test examines the null hypothesis that the time series has a unit root, which implies non-stationarity. Low p-values (typically below 0.05) lead to the rejection of the null hypothesis, suggesting that the time series is stationary.

## 5. What is a Markov process, and how is it applied in time series modeling?

A Markov process is a type of stochastic process where the future state of the process depends only on the present state, not on the entire past history.

This "memoryless" property simplifies modeling. In time series, AR(1) and AR(2) models are examples of Markov processes. A higher-order Markov process allows dependence on a finite number of previous states.

## 6. How do we analyze multivariate time series?

Multivariate time series involve multiple variables measured over time. To analyze these, we extend concepts from univariate time series:

- **Mean Vector:** Represents the average values of all variables at a given time.
- **Covariance Matrix:** Captures the variances and covariances between all pairs of variables at specific times.
- **Cross-Correlation:** Measures the correlation between different variables across various time lags.

## 7. What is Granger causality, and how is it tested?

Granger causality examines if one time series can predict another. It does not imply true causality but indicates predictive power. To test it, we compare two models:

1. **Unrestricted Model:** Includes past values of both time series to predict the future of one.
2. **Restricted Model:** Excludes past values of the potentially "Granger-causing" series.

An F-test comparing these models helps determine if the unrestricted model significantly improves prediction, suggesting Granger causality.

## 8. What Python libraries are commonly used for time series analysis and forecasting?

- **NumPy:** For numerical computing with arrays and matrices.
- **Pandas:** For data manipulation and analysis, particularly for time-indexed data.
- **Statsmodels:** For statistical modeling, including time series models like ARIMA.
- **SciPy:** For scientific computing, with tools for optimization and statistical analysis.
- **Matplotlib:** For data visualization, including plotting time series and ACFs.
- **Yfinance:** For downloading financial data.