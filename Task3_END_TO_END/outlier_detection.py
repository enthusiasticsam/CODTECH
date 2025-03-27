import pandas as pd
import numpy as np
from scipy import stats

# Load engineered data
data = pd.read_csv("data/engineered_bangalore_prices.csv")

# Detect outliers using Z-score for square_footage and price
z_scores_sqft = np.abs(stats.zscore(data["square_footage"]))
z_scores_price = np.abs(stats.zscore(data["price"]))
threshold = 3
data_no_outliers = data[(z_scores_sqft < threshold) & (z_scores_price < threshold)]

# Save data without outliers
data_no_outliers.to_csv("data/final_bangalore_prices.csv", index=False)
print("Data without outliers saved to 'data/final_bangalore_prices.csv'")