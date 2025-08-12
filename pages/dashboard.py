import streamlit as st
import google.generativeai as genai

def app():
    st.title("🏗️ ConstructAI Dashboard")
    st.write("Welcome! Please enter your Google API key to get started.")

    # Input for API key
    google_api_key = st.text_input("Enter your Google API key", type="password")

    # Save API key in session state
    if google_api_key:
        st.session_state["google_api_key"] = google_api_key
        st.success("✅ API key saved successfully!")

    # Check if API key is saved
    if "google_api_key" not in st.session_state:
        st.warning("⚠️ Please enter your API key above to enable AI features.")
        return

    # Configure Generative AI
    try:
        genai.configure(api_key=st.session_state["google_api_key"])
    except Exception as e:
        st.error(f"API Key Error: {e}")
        return

    if st.button("Test Available Models"):
        try:
            models = genai.list_models()
            model_names = [model.name for model in models]
            st.success(f"Found {len(model_names)} models.")
            model_selected = st.selectbox("Select a model to test:", model_names)

            prompt = st.text_area("Enter prompt to test the model:", "Hello, AI!")

            if st.button("Generate Response"):
                if not prompt.strip():
                    st.warning("Please enter a prompt.")
                else:
                    model = genai.GenerativeModel(model_selected)
                    response = model.generate_content(prompt)
                    st.subheader("Model Response")
                    st.write(response.text)
        except Exception as e:
            st.error(f"Error fetching models or generating content: {e}")
