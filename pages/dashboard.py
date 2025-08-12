import streamlit as st

def app():
    st.title("Dashboard")
    st.write("Welcome to ConstructAI dashboard! Please enter your Google API key to continue.")

    google_api_key = st.text_input("Enter your Google API key", type="password")

    if google_api_key:
        st.success("API key entered!")
        # Use google_api_key here for your API calls
    else:
        st.warning("Please enter your API key to use the app.")
