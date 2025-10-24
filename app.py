import streamlit as st
from datetime import datetime
import requests

'''
# TaxiFareModel
'''

'''
## Add your variables in order to receive a price estimation
'''
pickup_date = st.date_input("Pickup date")
pickup_time = st.time_input("Pickup time")

pickup_longitude = st.number_input("Pickup longitude")
pickup_latitude = st.number_input("Pickup latitude")
dropoff_longitude = st.number_input("Dropoff longitude")
dropoff_latitude = st.number_input("Dropoff latitude")
passenger_count = st.number_input("Passenger count", step=1)

# --- Combine date + time ---
pickup_datetime = datetime.combine(pickup_date, pickup_time).isoformat()


url = 'https://taxifare.lewagon.ai/predict'

params = dict(
    pickup_datetime=pickup_datetime,
    pickup_longitude=pickup_longitude,
    pickup_latitude=pickup_latitude,
    dropoff_longitude=dropoff_longitude,
    dropoff_latitude=dropoff_latitude,
    passenger_count=passenger_count)

wagon_cab_api_url = 'https://taxifare.lewagon.ai/predict'
response = requests.get(wagon_cab_api_url, params=params)


prediction = response.json().get("fare", "No fare found")
st.success(f"🚕 Estimated Fare: **${prediction:.2f}**")
