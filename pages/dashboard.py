import streamlit as st

def app():
    st.title("Dashboard")
    st.write("Welcome to ConstructAI dashboard! Your project overview will appear here.")

    # Safely get the API key from Streamlit secrets
    try:
        google_api_key = st.secrets["google_api_key"]
    except KeyError:
        st.error("API key not found! Please add 'google_api_key' to Streamlit secrets.")
        return

    # Show a masked version of the key to confirm it's loaded (first 4 chars + stars)
    masked_key = google_api_key[:4] + "****" + google_api_key[-4:]
    st.write(f"Google API key loaded: {masked_key}")

    # Placeholder for your actual dashboard logic where you use google_api_key
    # For example: call some Google API here using google_api_key

    # Example button to simulate API call
    if st.button("Test API Connection"):
        st.write("API key is ready to use! (Implement your API logic here.)")
