import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('house_price_pred_slr.pkl', 'rb'))

# Streamlit UI
st.title("House Price Prediction App")
st.write("Enter the area (in square feet) to predict the house price.")

# User input
area_sq_ft = st.number_input("Enter Area (sq ft)", min_value=1000, max_value=10000, step=10)

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(np.array([[area_sq_ft]]))
    st.success(f"🏠 Estimated House Price: ${prediction[0]:,.2f}")


