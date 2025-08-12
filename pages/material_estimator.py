import streamlit as st
import google.generativeai as genai

def app():
    st.title("Material Estimator")
    st.write("Estimate construction materials based on project details.")

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

    # Example prompt
    example_prompt = (
        "Estimate the quantity of concrete, steel, and bricks needed for a "
        "two-story residential building with 2000 sq ft floor area."
    )

    option = st.radio(
        "Choose an option:",
        ("Use example estimation", "Provide project details")
    )

    prompt = ""

    if option == "Use example estimation":
        prompt = example_prompt
        st.info(f"Using example:\n\n{prompt}")
    else:
        prompt = st.text_area("Enter your project details for material estimation:")

    if st.button("Estimate Materials"):
        if not prompt:
            st.warning("Please enter project details to estimate materials.")
            return
        try:
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt)
            st.subheader("🧮 Material Estimation Result")
            st.write(response.text)
        except Exception as e:
            st.error(f"AI Error: {e}")
