# streamlit_app/pages/survey.py
import sys
from pathlib import Path

# Adds the root project directory to sys.path
sys.path.append(str(Path(__file__).resolve().parents[2]))
import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_app.database.db import create_response_table, insert_response
create_response_table()# make sure table exists at import time
create_response_table()

st.set_page_config(page_title="Survey")
st.title("Vehicle Preference Questionnaire")
st.write("Please fill out the form below to tell me about your favorite vehicle:")

with st.form("questionnaire_form"):
    current_year = datetime.now().year
    name               = st.text_input("Your Name")
    car_name           = st.text_input("Current Vehicle's Name (if applicable)")
    car_model          = st.text_input("Current Vehicle's Make & Model")
    current_model_year = st.number_input(
        "Current Vehicle's Model Year",
        min_value=1900,
        max_value=current_year + 1,
        step=1
    )
    purchase_year = st.number_input(
        "In What Year Did You Buy This Car?",
        min_value=1900,
        max_value=current_year,
        step=1
    )

    likert_rating = st.radio(
        "How much did you like this vehicle?",
        ["Not at all", "A little", "Neutral", "A lot", "Very much"],
        horizontal=True
    )

    st.markdown("----")
    st.subheader("Tell me about a vehicle you'd like to own in the future")

    dream_vehicle      = st.text_input("Future Vehicle's Make & Model", value="Chevrolet Silverado")
    future_model_year  = st.number_input(
        "Future Vehicle's Year",
        min_value=1900,
        max_value=current_year + 1,
        step=1,
        value=current_year + 1
    )
    preferred_color    = st.text_input("Future Vehicle's Preferred Color", value="White")
    vehicle_type       = st.selectbox("What Type of Vehicle Is This?", ["Car", "Truck", "SUV", "Other"])
    powerplant         = st.radio("Preferred Powerplant", ["Gas/ICE", "Electric"])

    submitted = st.form_submit_button("Submit")

def save_response_to_excel(response_dict, excel_path):
    # Convert single record to a DataFrame
    df = pd.DataFrame([response_dict])

    # If the file already exists, append to it
    if excel_path.exists():
        existing_df = pd.read_excel(excel_path)
        combined_df = pd.concat([existing_df, df], ignore_index=True)
    else:
        combined_df = df

    # Save the updated DataFrame to Excel
    combined_df.to_excel(excel_path, index=False)

if submitted:
    response_data = {
        "name": name,
        "car_name": car_name,
        "car_model": car_model,
        "current_model_year": current_model_year,
        "purchase_year": purchase_year,
        "likert_rating": likert_rating,
        "dream_vehicle": dream_vehicle,
        "future_purchase_year": future_model_year,
        "preferred_color": preferred_color,
        "vehicle_type": vehicle_type,
        "powerplant": powerplant,
    }
    insert_response(response_data)
        # Excel path: project/survey_responses.xlsx
    excel_path = Path(__file__).resolve().parent.parent.parent / "survey_responses.xlsx"
    save_response_to_excel(response_data, excel_path)
    st.success("✅ Thank you for submitting the survey!")