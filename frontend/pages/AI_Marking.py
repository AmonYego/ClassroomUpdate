import sys
import os
import streamlit as st

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from frontend.utils.api_client import mark_answer
from frontend.StudyBuddy import level
st.title("📝 Get Your Work Marked")
st.write(
    "Upload your completed answers, and I'll provide a detailed evaluation and score."
)

question_file = st.file_uploader(
    "Upload your answers here", type=["pdf", "docx", "txt"]
)

if st.button("Mark My Work"):
    if not question_file:
        st.warning("Please upload your answers to continue.")
    elif level == "--Select Level--":
        st.warning("Please select your education level to continue.")
    else:
        with st.spinner("Evaluating your answers... 🧑‍🏫"):
            response = mark_answer(question_file, level)
            st.write(response)
