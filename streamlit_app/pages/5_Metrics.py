"""
This page is intended to track and evaluate user metadata.
"""

import streamlit as st
import pandas as pd
from streamlit_app.database.db import get_all_signins

def show():
    st.set_page_config(page_title="Metrics Dashboard")
    st.header("Sign-On Metadata Dashboard")

    # Retrieve data from local SQLite DB
    data = get_all_signins()

    if not data:
        st.warning("No sign-in records found.")
        return

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=["Name", "Email", "Username", "Password", "Login Time"])
    df["Login Time"] = pd.to_datetime(df["Login Time"])

    # Display key metrics
    st.subheader("Sign-In Statistics")
    st.metric("Total Sign-Ins", len(df))
    st.metric("Unique Users", df["Username"].nunique())
    st.metric("Most Recent Sign-In", df.iloc[0]["Login Time"].strftime("%B %d, %Y at %I:%M:%S %p"))

    # Display full log
    st.subheader("Sign-In Log")
    st.dataframe(df)

    # Filter by user
    st.subheader("Filter by Username")
    usernames = df["Username"].unique()
    selected = st.selectbox("Select a user", usernames)
    st.dataframe(df[df["Username"] == selected])

show()