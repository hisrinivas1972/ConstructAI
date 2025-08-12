import streamlit as st
import google.generativeai as genai

def app():
    st.title("Schedule Optimizer")
    st.write("Optimize your construction schedule with AI assistance.")

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
        "Optimize the schedule for a 6-month residential construction project with possible weather delays."
    )

    option = st.radio(
        "Choose an option:",
        ("Use example schedule", "Enter your own schedule details")
    )

    prompt = ""

    if option == "Use example schedule":
        prompt = example_prompt
        st.info(f"Using example:\n\n{prompt}")
    else:
        prompt = st.text_area("Enter schedule details or constraints:")

    if st.button("Optimize Schedule"):
        if not prompt:
            st.warning("Please enter schedule details to optimize.")
            return
        try:
            model = genai.GenerativeModel("models/chat-bison-001")
            response = model.generate_content(prompt)
            st.subheader("📅 Optimized Schedule")
            st.write(response.text)
        except Exception as e:
            st.error(f"AI Error: {e}")
