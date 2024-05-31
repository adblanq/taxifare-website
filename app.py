import streamlit as st
import requests
from datetime import datetime

st.set_page_config(layout="wide")

'''
# TaxiFareModel front
'''

url = 'https://taxifare-api-adblanq-ugx7qewr7q-ew.a.run.app/predict'

with st.form("predict_fare"):
    cols = st.columns(7)

    with cols[0]:
        pickup_long = st.text_input("Pickup longitude", value=-73.950655)
    with cols[1]:
        pickup_lat = st.text_input("Pickup latitude", value=40.783282)
    with cols[2]:
        drop_long = st.text_input("Dropoff longitude", value=-73.984365)
    with cols[3]:
        drop_lat = st.text_input("Dropoff latitude", value=40.769802)
    with cols[4]:
        date = st.date_input("Date", value=datetime.strptime("2014-07-06", "%Y-%M-%d"))
    with cols[5]:
        passenger = st.text_input("Passenger(s)", value=2)
    with cols[6]:
        submited = st.form_submit_button("Estimate")


    if submited:
        params = {
            "pickup_datetime": date,
            "pickup_longitude": pickup_long,
            "pickup_latitude": pickup_lat,
            "dropoff_longitude": drop_long,
            "dropoff_latitude": drop_lat,
            "passenger_count": passenger
        }

        response = requests.get(url, params=params).json()
        st.write(response)
