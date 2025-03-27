import pandas as pd

# Load the dataset
data = pd.read_csv("data/bangalore_house_prices.csv")

# Handle missing values
print("Missing values:\n", data.isnull().sum())
data["square_footage"].fillna(data["square_footage"].median(), inplace=True)

# Basic cleaning
data = data.dropna()
data = data[data["square_footage"] > 0]
data = data[data["price"] > 0]

# Save cleaned data
data.to_csv("data/cleaned_bangalore_prices.csv", index=False)
print("Cleaned data saved to 'data/cleaned_bangalore_prices.csv'")