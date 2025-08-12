import streamlit as st

def app():
    st.title("Dashboard")
    st.write("Welcome to ConstructAI dashboard! Please enter your Google API key to continue.")

    # Password input box (hides input)
    google_api_key = st.text_input("Enter your Google API key", type="password")

    if google_api_key:
        st.success("API key entered!")
        # You can safely use google_api_key here for your API calls
        # For demo, show masked key:
        masked_key = google_api_key[:4] + "****" + google_api_key[-4:]
        st.write(f"Using API key: {masked_key}")

        # Placeholder: call your Google API functions here with google_api_key

    else:
        st.warning("Please enter your API key to use the app.")
