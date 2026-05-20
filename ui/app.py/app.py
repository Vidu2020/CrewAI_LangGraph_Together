import streamlit as st
import requests

st.set_page_config(page_title="LLM Factory", layout="wide")

st.title("🏭 LLM Factory (CrewAI + LangGraph)")
st.markdown("Generate AI-powered business reports")

# Input
topic = st.text_input("Enter Topic", "Future of Agentic AI")

# Submit button
if st.button("Generate Report"):

    with st.spinner("Running AI agents... ⏳"):
        response = requests.post(
            "http://127.0.0.1:8000/generate",
            params={"topic": topic}
        )

    if response.status_code == 200:
        result = response.json()["result"]

        st.success("✅ Report Generated")

        st.text_area("Final Report", str(result), height=400)

    else:
        st.error("❌ Failed to generate report")
