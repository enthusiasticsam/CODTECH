import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Load final data
data = pd.read_csv("data/final_bangalore_prices.csv")

# One-hot encode the 'area' column
data = pd.get_dummies(data, columns=["area"], drop_first=True)

# Features and target
X = data.drop(["price", "price_per_sqft"], axis=1)  # Drop price and price_per_sqft
y = data["price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate
y_pred = model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Save model and scaler
joblib.dump(model, "bangalore_price_model.pkl")
joblib.dump(scaler, "bangalore_scaler.pkl")
print("Model and scaler saved!")