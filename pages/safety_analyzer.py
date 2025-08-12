import streamlit as st
import google.generativeai as genai

def app():
    st.title("Safety Analyzer")
    st.write("Analyze construction site safety using AI.")

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
        "A crane is operating near live power lines without a spotter. "
        "Workers are not wearing helmets in the vicinity."
    )

    # Ask user how to proceed
    prompt_option = st.radio(
        "How would you like to proceed?",
        ["Use example prompt", "Write my own scenario", "Upload construction site image"]
    )

    prompt = ""
    image = None

    if prompt_option == "Use example prompt":
        prompt = default_prompt
        st.info(f"Using example scenario:\n\n{prompt}")

    elif prompt_option == "Write my own scenario":
        prompt = st.text_area("Enter your safety scenario:")

    else:
        image = st.file_uploader("Upload Construction Site Image", type=["jpg", "jpeg", "png"])

    if st.button("Analyze Safety"):
        if prompt_option in ["Use example prompt", "Write my own scenario"] and not prompt:
            st.warning("Please enter a safety scenario to analyze.")
            return

        if prompt_option == "Upload construction site image" and image is None:
            st.warning("Please upload an image to analyze.")
            return

        try:
            model = genai.GenerativeModel("gemini-pro")

            if prompt_option in ["Use example prompt", "Write my own scenario"]:
                response = model.generate_content(prompt)
            else:
                # For demo, just acknowledge image upload since Google Gen AI image analysis
                # may require special API calls — replace with your logic
                response = model.generate_content(
                    "Analyze safety risks based on the following construction site image."
                )

            st.subheader("🧠 AI Safety Analysis")
            st.write(response.text)

            if image:
                st.image(image, caption="Uploaded Site Image", use_column_width=True)

        except Exception as e:
            st.error(f"AI Error: {e}")
