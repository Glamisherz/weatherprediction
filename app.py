import streamlit as st
import joblib
import pandas as pd
import numpy as np


model = joblib.load("model.pkl")

st.set_page_config(page_title="🌤️ Climate Temperature Predictor", layout="centered")
st.title("🌤️ Predict Temperature from Weather Data")

st.markdown("Enter the weather conditions to get the predicted temperature.")


humidity = st.number_input("Humidity (%)", value=75.0)
wind_speed = st.number_input("Wind Speed (km/h)", value=7.2)
rainfall = st.number_input("Rainfall (mm)", value=1.8)
max_temp = st.number_input("Max Temperature (°C)", value=30.0)
min_temp = st.number_input("Min Temperature (°C)", value=20.0)
dew_point = st.number_input("Dew Point (°C)", value=25.0)
pressure = st.number_input("Pressure (hPa)", value=1015.0)
visibility = st.number_input("Visibility (km)", value=10.0)
cloud_cover = st.number_input("Cloud Cover (%)", value=10.0)
solar_radiation = st.number_input("Solar Radiation (MJ/m²)", value=25.0)
day = st.number_input("Day", min_value=1, max_value=31, value=19)
month = st.number_input("Month", min_value=1, max_value=12, value=5)
year = st.number_input("Year", min_value=2000, max_value=2100, value=2025)

weather_condition = st.selectbox("Weather Condition", ["Foggy", "Rainy", "Stormy"])
weather_dict = {
    'weather_condition_Foggy': 0,
    'weather_condition_Rainy': 0,
    'weather_condition_Stormy': 0
}
weather_dict[f'weather_condition_{weather_condition}'] = 1


if st.button("Predict Temperature"):
    
    input_dict = {
        'humidity': humidity,
        'wind_speed': wind_speed,
        'rainfall': rainfall,
        'max_temperature': max_temp,
        'min_temperature': min_temp,
        'dew_point': dew_point,
        'pressure': pressure,
        'visibility': visibility,
        'cloud_cover': cloud_cover,
        'solar_radiation': solar_radiation,
        'day': day,
        'month': month,
        'year': year,
        **weather_dict
    }

    input_df = pd.DataFrame([input_dict])
    prediction = model.predict(input_df)[0]
    st.success(f"🌡️ Predicted Temperature: **{prediction:.2f} °C**")
