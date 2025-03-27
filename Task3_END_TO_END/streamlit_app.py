import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model and scaler
try:
    model = joblib.load(r"Task3_END_TO_END\bangalore_price_model.pkl")
    scaler = joblib.load(r"Task3_END_TO_END\bangalore_scaler.pkl")
except FileNotFoundError:
    st.error("Model or scaler file not found. Run train_model.py first.")
    st.stop()

# List of areas (sorted alphabetically to match training)
areas = sorted([
    "Koramangala", "Indiranagar", "Whitefield", "Yelahanka", "Jayanagar",
    "Kengeri", "HSR Layout", "Marathahalli", "Banashankari", "Electronic City"
])

# Streamlit UI
st.title("🏠 Bangalore House Price Prediction")
st.markdown("Enter house details to predict the price in Bangalore (in INR Lakhs).")

# Input fields
col1, col2 = st.columns(2)
with col1:
    square_footage = st.number_input("Square Footage", min_value=500, max_value=5000, value=2000, step=100)
    bedrooms = st.number_input("Bedrooms", min_value=1, max_value=6, value=3)
with col2:
    bathrooms = st.number_input("Bathrooms", min_value=1, max_value=6, value=2)
    area = st.selectbox("Area", areas)

# Calculate rooms_total
rooms_total = bedrooms + bathrooms

# Prepare features for prediction
if st.button("Predict Price"):
    # Create a DataFrame with the input features
    input_data = pd.DataFrame({
        "square_footage": [square_footage],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "rooms_total": [rooms_total]
    })

    # One-hot encode the area (same as training)
    area_encoded = pd.get_dummies(pd.Series([area]), prefix="area")
    # Reindex to match the training features (drop_first=True in training)
    training_area_columns = [f"area_{a}" for a in areas[1:]]  # Exclude the first area (Banashankari)
    area_encoded = area_encoded.reindex(columns=training_area_columns, fill_value=0)

    # Combine input data with encoded area
    input_data = pd.concat([input_data, area_encoded], axis=1)

    # Scale features and predict
    try:
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)
        price_lakhs = prediction[0] / 100000
        st.success(f"Predicted House Price: **₹{price_lakhs:,.2f} Lakhs**")
    except Exception as e:
        st.error(f"Prediction failed: {str(e)}")

# Footer
st.markdown("---")
st.write("Based on a Bangalore dataset. Results are indicative.")