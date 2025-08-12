import streamlit as st
import time

def app():
    st.title("Productivity Reporter")
    google_api_key = st.secrets["google_api_key"]

    input_text = st.text_area("Project Progress Description", height=200)

    if st.button("Generate Productivity Report"):
        if input_text.strip() == "":
            st.warning("Please enter project progress description.")
        else:
            with st.spinner("Generating report..."):
                time.sleep(2)
                # Use google_api_key with your API call here for AI report generation
            st.markdown("""
            **Summary:**  
            The project progressed well with completed foundation work and steel framing started.

            **Challenges:**  
            Weather delays caused a 2-day setback.

            **Next Steps:**  
            Monitor progress, adjust schedules, and mitigate weather risks.
            """)
