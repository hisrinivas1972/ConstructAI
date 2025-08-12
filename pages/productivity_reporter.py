import streamlit as st
import google.generativeai as genai

def app():
    st.title("Productivity Reporter")
    st.write("Report and analyze construction site productivity.")

    # Get the API key from session state
    google_api_key = st.session_state.get("google_api_key", "")
    if not google_api_key:
        st.warning("⚠️ Please enter your Google API key on the Dashboard first.")
        return

    # Configure Generative AI with the user’s key
    try:
        genai.configure(api_key=google_api_key)
    except Exception as e:
        st.error(f"API Key Error: {e}")
        return

    st.success("✅ API key loaded. Gemini AI is ready.")

    # Default example prompt
    default_prompt = (
        "Workers are experiencing delays due to unexpected equipment failure. "
        "Please summarize the impact on productivity."
    )

    prompt_option = st.radio(
        "How would you like to proceed?",
        ["Use example report", "Write my own report"]
    )

    prompt = ""

    if prompt_option == "Use example report":
        prompt = default_prompt
        st.info(f"Using example report:\n\n{prompt}")
    else:
        prompt = st.text_area("Enter your productivity report or issue description:")

    if st.button("Analyze Productivity"):
        if not prompt:
            st.warning("Please enter a productivity report or issue to analyze.")
            return

        try:
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt)
            st.subheader("🧠 AI Productivity Analysis")
            st.write(response.text)
        except Exception as e:
            st.error(f"AI Error: {e}")
