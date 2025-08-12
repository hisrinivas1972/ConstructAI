import streamlit as st
import openai

def app():
    st.title("Floor Plan Visualizer")
    google_api_key = st.secrets["google_api_key"]

    desc = st.text_area("Floor Plan Description", height=200,
        placeholder="Describe the rooms, dimensions, doors, windows, etc.")

    exclude = st.text_area("Elements to Exclude (Optional)")

    if st.button("Generate Floor Plan"):
        if desc.strip() == "":
            st.warning("Please enter a floor plan description.")
        else:
            with st.spinner("Generating floor plan..."):
                # Example call to OpenAI's image generation API
                openai.api_key = google_api_key
                prompt = desc
                if exclude.strip():
                    prompt += f" Exclude: {exclude}."
                response = openai.Image.create(
                    prompt=prompt,
                    n=1,
                    size="512x512"
                )
                image_url = response['data'][0]['url']
                st.image(image_url, caption="AI-generated Floor Plan")

