import streamlit as st
import requests
from datetime import datetime

# --- Page setup ---
st.title("🚕 TaxiFareModel")
st.markdown("Enter your trip details below to get an estimated fare.")

# --- Input fields ---
pickup_date = st.date_input("Pickup date")
pickup_time = st.time_input("Pickup time")

pickup_longitude = st.number_input("Pickup longitude", value=-73.985428, format="%.6f")
pickup_latitude = st.number_input("Pickup latitude", value=40.748817, format="%.6f")
dropoff_longitude = st.number_input("Dropoff longitude", value=-73.985000, format="%.6f")
dropoff_latitude = st.number_input("Dropoff latitude", value=40.730610, format="%.6f")
passenger_count = st.number_input("Passenger count", min_value=1, max_value=8, value=1, step=1)

# --- Combine date + time ---
pickup_datetime = datetime.combine(pickup_date, pickup_time).isoformat()

# --- API URL ---
url = "https://taxifare.lewagon.ai/predict"

# --- Predict button ---
if st.button("Predict fare"):
    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # raise an error for bad responses
        result = response.json()
        fare = result.get("fare")
        if fare is not None:
            st.success(f"💰 Estimated fare: **${fare:.2f}**")
        else:
            st.warning("No fare returned from the API.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error contacting the API: {e}")
