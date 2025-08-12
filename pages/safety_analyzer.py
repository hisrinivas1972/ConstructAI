import streamlit as st
import google.generativeai as genai

def app():
    st.title("Safety Analyzer")
    st.write("Analyze construction site safety using AI.")

    google_api_key = st.session_state.get("google_api_key", "")
    if not google_api_key:
        st.warning("⚠️ Please enter your Google API key on the Dashboard first.")
        return

    try:
        genai.configure(api_key=google_api_key)
    except Exception as e:
        st.error(f"API Key Error: {e}")
        return

    st.success("✅ API key loaded. Gemini AI is ready.")

    prompt = st.text_area("Enter a safety scenario, observation, or concern:")

    if st.button("Analyze Safety"):
        if not prompt:
            st.warning("Please enter a scenario or observation to analyze.")
            return

        try:
            model = genai.GenerativeModel("models/chat-bison-001")
            response = model.generate_content(prompt)
            st.subheader("🧠 AI Safety Analysis")
            st.write(response.text)
        except Exception as e:
            st.error(f"AI Error: {e}")
