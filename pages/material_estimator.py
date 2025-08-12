import streamlit as st
import google.generativeai as genai

def app():
    st.title("Material Estimator")
    st.write("Estimate construction materials needed using AI.")

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
        "Estimate the quantity of cement, sand, gravel, and bricks needed for building a 1000 sq ft house."
    )

    option = st.radio(
        "Choose an option:",
        ("Use example estimation", "Enter your own material requirements")
    )

    prompt = ""

    if option == "Use example estimation":
        prompt = example_prompt
        st.info(f"Using example:\n\n{prompt}")
    else:
        prompt = st.text_area("Enter details for material estimation:")

    if st.button("Estimate Materials"):
        if not prompt:
            st.warning("Please enter details to estimate materials.")
            return
        try:
            model = genai.GenerativeModel("models/chat-bison-001")
            response = model.generate_content(prompt)
            st.subheader("🧱 Material Estimation")
            st.write(response.text)
        except Exception as e:
            st.error(f"AI Error: {e}")
