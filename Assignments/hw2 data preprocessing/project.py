# Project: Energy Consumption Data Analysis
# Author: Tony Wang
# Date: 2024-10-24

## 1. Data Collection

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
data = pd.read_csv('energy_consumption.csv')

# Display the first few rows of the dataset
print(data.head())

## 2. Data Preprocessing

    
