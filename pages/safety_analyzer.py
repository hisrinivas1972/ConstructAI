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

    example_prompt = (
        "Identify potential safety hazards from this site description: "
        "Workers are using scaffolding without harnesses near high-voltage lines."
    )

    option = st.radio(
        "Choose an option:",
        ("Use example safety scenario", "Enter your own safety observation")
    )

    prompt = ""

    if option == "Use example safety scenario":
        prompt = example_prompt
        st.info(f"Using example:\n\n{prompt}")
    else:
        prompt = st.text_area("Enter safety scenario or observation:")

    if st.button("Analyze Safety"):
        if not prompt:
            st.warning("Please enter a safety scenario or observation.")
            return
        try:
            model = genai.GenerativeModel("models/chat-bison-001")  # update with valid model if needed
            response = model.generate_content(prompt)
            st.subheader("🧠 AI Safety Analysis")
            st.write(response.text)
        except Exception as e:
            st.error(f"AI Error: {e}")
