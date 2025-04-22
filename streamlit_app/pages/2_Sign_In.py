# streamlit_app/pages/sign_in.py
import sys
from pathlib import Path

# Adds the root project directory to sys.path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from datetime import datetime
from streamlit_app.database.db import create_signin_table, insert_signin

create_signin_table()

if "signed_in" not in st.session_state:
    st.session_state.signed_in = False

def reset_signin():
    st.session_state.signed_in = False
    st.session_state.username = ""
    st.rerun()

def show():
    st.set_page_config(page_title="Sign In")
    st.header("🔐 Sign In")

    if st.session_state.signed_in:
        st.success(f"Welcome: {st.session_state.username}!")

        # Add reset button
        if st.button("🔁 Reset Sign-In"):
            reset_signin()
        return

    with st.form("login_form"):
        name     = st.text_input("Name")
        email    = st.text_input("Email")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Sign In")

    if submitted:
        if not (name and email and username and password):
            st.error("Please fill in all fields.")
            return

        now = datetime.now().isoformat()
        insert_signin(name, email, username, password, now)

        st.session_state.signed_in = True
        st.session_state.username  = username
        st.success("✅ Signed in successfully!")
        st.rerun()
show()