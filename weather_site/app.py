import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🌤️ Monthly weather data")

data = {
    "Month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ],
    "Average Temperature (℃)": [3, 5, 9, 15, 20, 24, 28, 30, 26, 18, 11, 5],
    "Precipitation (mm)": [45, 50, 90, 110, 130, 160, 180, 170, 140, 100, 70, 50],
    "Humidity (%)": [65, 60, 58, 60, 68, 75, 80, 82, 78, 70, 66, 64],
}

df = pd.DataFrame(data)

st.subheader("📊 Weather Data Table")
st.dataframe(df)

st.subheader("📈 Trends of Average Temperature and Humidity")
st.line_chart(df.set_index("Month")[["Average Temperature (℃)", "Humidity (%)"]])

st.subheader("🌧️ Monthly Precipitation")
fig, ax = plt.subplots()
ax.bar(df["Month"], df["Precipitation (mm)"], color="skyblue")
ax.set_xlabel("Month")
ax.set_title("Monthy Precipitation")
st.pyplot(fig)
