import streamlit as st

def app():
    st.title("Dashboard")
    st.write("Welcome to ConstructAI dashboard! Please enter your Google API key to continue.")

    # Check if API key already in session state, set default for input box
    default_key = st.session_state.get("google_api_key", "")

    # Input box to accept the API key (hidden), pre-filled if already stored
    google_api_key = st.text_input("Enter your Google API key", type="password", value=default_key)

    # When user inputs or changes key, update session state
    if google_api_key != default_key:
        st.session_state["google_api_key"] = google_api_key
        st.success("✅ API key saved successfully!")

    if not google_api_key:
        st.warning("⚠️ Please enter your API key to use the app.")
    else:
        st.info("🔐 API key is set. You can use other tools from the sidebar.")
