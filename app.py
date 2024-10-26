import streamlit as st
import numpy as np
import pickle

# Load your saved model
with open('credit_score_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define your prediction function
def predict_credit_score(input_data):
    data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(data)
    return prediction

st.title('Credit Score Prediction App')

luxury_spending = st.number_input('Luxury Spending', min_value=0)
charity_spending = st.number_input('Charity Spending', min_value=0)
local_business_spending = st.number_input('Small/Local Business Spending', min_value=0)
groceries = st.number_input('Groceries/Food Spending', min_value=0)
transportation = st.number_input('Transportation Spending', min_value=0)
clothing_shopping = st.number_input('Clothing/Shopping Spending', min_value=0)
electronics = st.number_input('Electronics Spending', min_value=0)
utilities = st.number_input('Utilities Spending', min_value=0)
entertainment = st.number_input('Entertainment Spending', min_value=0)
other_services = st.number_input('Other Services Spending', min_value=0)

if st.button('Predict Credit Score'):
    input_data = [
        luxury_spending,
        charity_spending,
        local_business_spending,
        groceries,
        transportation,
        clothing_shopping,
        electronics,
        utilities,
        entertainment,
        other_services
    ]
    prediction = predict_credit_score(input_data)
    st.success(f'Predicted Credit Score: {prediction[0]}')
