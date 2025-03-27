import pandas as pd

# Load cleaned data
print("Loading data...")
data = pd.read_csv("data/cleaned_bangalore_prices.csv")
print("Data loaded successfully. Shape:", data.shape)

# Feature engineering
data["rooms_total"] = data["bedrooms"] + data["bathrooms"]
data["price_per_sqft"] = data["price"] / data["square_footage"]
print("Features added. First row:\n", data.head(1))

# Save engineered data
data.to_csv("data/engineered_bangalore_prices.csv", index=False)
print("Engineered data saved to 'data/engineered_bangalore_prices.csv'")