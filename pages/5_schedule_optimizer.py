import streamlit as st
import time

def app():
    st.title("Schedule Optimizer")
    google_api_key = st.secrets["google_api_key"]

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant",
                                      "content": "Hi! I can help optimize your construction schedule. Tell me about your project."}]

    for msg in st.session_state.messages:
        if msg["role"] == "assistant":
            st.markdown(f"**Assistant:** {msg['content']}")
        else:
            st.markdown(f"**You:** {msg['content']}")

    prompt = st.text_input("Ask about scheduling or resources")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner("Optimizing schedule..."):
            time.sleep(2)
            response = "Based on your input, here’s a suggested schedule with optimized resource allocation."
            st.session_state.messages.append({"role": "assistant", "content": response})
        st.experimental_rerun()
