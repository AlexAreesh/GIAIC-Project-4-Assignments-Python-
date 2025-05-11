
import streamlit as st

st.title("BMI Calculator")
w = st.number_input("Weight (kg)")
h = st.number_input("Height (m)")

if w and h:
    bmi = w / (h * h)
    st.write("BMI is", round(bmi, 2))
