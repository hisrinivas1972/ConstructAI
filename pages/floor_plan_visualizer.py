import streamlit as st
import google.generativeai as genai

def app():
    st.title("Floor Plan Visualizer")
    st.write("Generate and visualize construction floor plans using AI.")

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

    # Example prompt for floor plan visualization
    example_prompt = (
        "Generate a floor plan for a 3-bedroom, 2-bathroom house with an open-concept kitchen and living area."
    )

    option = st.radio(
        "Choose an option:",
        ("Use example floor plan", "Describe your floor plan requirements")
    )

    prompt = ""

    if option == "Use example floor plan":
        prompt = example_prompt
        st.info(f"Using example:\n\n{prompt}")
    else:
        prompt = st.text_area("Enter your floor plan requirements:")

    if st.button("Generate Floor Plan"):
        if not prompt:
            st.warning("Please enter floor plan requirements.")
            return
        try:
            model = genai.GenerativeModel("gemini-2.0-flash-exp-image-generation")
            response = model.generate_content(prompt)
            st.subheader("🏠 Generated Floor Plan")
            st.write(response.text)
        except Exception as e:
            st.error(f"AI Error: {e}")
