import streamlit as st
import google.generativeai as genai

def app():
    st.title("Productivity Reporter")
    st.write("Generate productivity reports and insights using AI.")

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

    example_prompt = (
        "Summarize the productivity of a construction crew that completed 50% of the scheduled work "
        "in half the expected time but faced delays due to weather."
    )

    option = st.radio(
        "Choose an option:",
        ("Use example report", "Enter your own data or observations")
    )

    prompt = ""

    if option == "Use example report":
        prompt = example_prompt
        st.info(f"Using example:\n\n{prompt}")
    else:
        prompt = st.text_area("Enter your data or observations:")

    if st.button("Generate Report"):
        if not prompt:
            st.warning("Please enter data or observations to generate report.")
            return
        try:
            model = genai.GenerativeModel("models/chat-bison-001")
            response = model.generate_content(prompt)
            st.subheader("📊 Productivity Report")
            st.write(response.text)
        except Exception as e:
            st.error(f"AI Error: {e}")
