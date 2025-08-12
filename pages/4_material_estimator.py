import streamlit as st
import time

def app():
    st.title("Material Estimator")
    google_api_key = st.secrets["google_api_key"]

    project_desc = st.text_area("Project Description", height=200,
        placeholder="E.g., 'Build a 20x30 foot wooden shed...'")

    if st.button("Estimate Materials"):
        if project_desc.strip() == "":
            st.warning("Please enter project description.")
        else:
            with st.spinner("Estimating materials..."):
                time.sleep(2)
                # Call Google or other API here with google_api_key to estimate materials
            st.markdown("""
            **Material List:**  
            - Concrete: 6 cubic yards  
            - Lumber: 150 pieces  
            - Asphalt Shingles: 12 bundles  
            - Nails: 10 lbs  
            """)
