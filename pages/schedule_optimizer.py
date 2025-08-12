import streamlit as st
import google.generativeai as genai

def app():
    st.title("Schedule Optimizer")
    st.write("Optimize construction project schedules for better efficiency.")

    # Get API key from session state
    google_api_key = st.session_state.get("google_api_key", "")
    if not google_api_key:
        st.warning("⚠️ Please enter your Google API key on the Dashboard first.")
        return

    # Configure Google Generative AI
    try:
        genai.configure(api_key=google_api_key)
    except Exception as e:
        st.error(f"API Key Error: {e}")
        return

    st.success("✅ API key loaded. Gemini AI is ready.")

    # Example prompt for scheduling optimization
    example_prompt = (
        "Optimize the schedule for a commercial building construction project "
        "with 10 tasks, dependencies, and a tight deadline of 6 months."
    )

    option = st.radio(
        "Choose an option:",
        ("Use example schedule", "Provide your project schedule details")
    )

    prompt = ""

    if option == "Use example schedule":
        prompt = example_prompt
        st.info(f"Using example:\n\n{prompt}")
    else:
        prompt = st.text_area("Enter your project schedule details:")

    if st.button("Optimize Schedule"):
        if not prompt:
            st.warning("Please enter schedule details to optimize.")
            return
        try:
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt)
            st.subheader("📅 Optimized Schedule")
            st.write(response.text)
        except Exception as e:
            st.error(f"AI Error: {e}")
