import streamlit as st

def app():
    st.title("🏗️ ConstructAI Dashboard")
    st.write("Welcome to ConstructAI dashboard! Please enter your Google API key to continue.")

    # Input box to accept the API key (hidden)
    google_api_key = st.text_input("Enter your Google API key", type="password")

    # Save to session_state if provided
    if google_api_key:
        st.session_state["google_api_key"] = google_api_key
        st.success("✅ API key saved successfully!")
    else:
        # If already in session, show it’s still available
        if "google_api_key" in st.session_state:
            st.info("🔐 API key already set. You can use other tools from the sidebar.")
        else:
            st.warning("⚠️ Please enter your API key to use the app.")

    # You can add dashboard-specific content here, e.g. summary or stats
    st.markdown("---")
    st.write("Your project overview will appear here.")
