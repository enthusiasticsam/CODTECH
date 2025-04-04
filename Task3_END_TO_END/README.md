#Task-3 END-TO-END DATA SCIENCE PROJECT#

COMPANY: CODTECH IT SOLUTIONS

NAME: SHAIK SAMEENA

INTERN ID: CT08VQW

DOMAIN: DATA SCIENCE

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

This project, titled "Bangalore House Price Prediction," is an end-to-end data science application developed to predict house prices in Bangalore based on key property features. The objective is to create a practical solution where users can input house details and receive an estimated price in Indian Rupees (INR) lakhs. The project encompasses the entire machine learning pipeline, from data collection and preprocessing to model training and deployment, fulfilling the requirements of an internship task to develop a full data science project and deliver a deployed web application.

Due to the unavailability of comprehensive real-world Bangalore housing datasets, a synthetic dataset of 50 houses was generated. The dataset includes features such as square footage, number of bedrooms, bathrooms, and the area (e.g., Koramangala, Indiranagar, Whitefield). To simulate real-world data challenges, missing values and outliers were introduced. Data preprocessing was conducted in multiple stages: clean_data.py addresses missing values by imputing them (e.g., filling square_footage with the mean), feature_engineering.py creates derived features like rooms_total (sum of bedrooms and bathrooms) and price_per_sqft, and outlier_detection.py removes outliers using Z-score analysis. The processed dataset is saved as final_bangalore_prices.csv for modeling.

The predictive model was built using a Random Forest Regressor, selected for its ability to handle non-linear relationships in data. In train_model.py, the dataset is split into training and testing sets, the categorical area feature is one-hot encoded, and numerical features like square_footage are scaled using StandardScaler. The model is trained, evaluated using Mean Squared Error (MSE), and saved as bangalore_price_model.pkl along with the scaler (bangalore_scaler.pkl) using Joblib. While the current MSE is relatively high, indicating room for improvement, the model provides reasonable predictions given the dataset’s size.

To enable user interaction, a web application was developed using Streamlit. The streamlit_app.py script allows users to input property details, including square footage, number of bedrooms, bathrooms, and an area selected from a dropdown menu featuring 10 Bangalore neighborhoods (e.g., Jayanagar, HSR Layout). The application calculates rooms_total, applies the necessary scaling, and uses the trained model to predict the house price, displaying the result in INR lakhs (e.g., “Predicted House Price: ₹45.67 Lakhs”). The interface is intuitive and designed for ease of use.

As a deliverable, the application was deployed on Streamlit Community Cloud, making it publicly accessible via a URL. This deployment ensures that users can interact with the model’s functionality without needing to install any software. The project was developed using Python, leveraging libraries such as Pandas, NumPy, Scikit-learn, Joblib, and Streamlit, with all code and data hosted in a GitHub repository.

This project demonstrates a comprehensive data science workflow, including data generation, preprocessing, feature engineering, model training, evaluation, and deployment. It serves as a practical example of applying machine learning to real estate analytics, with potential for further enhancement in model accuracy and feature expansion.
