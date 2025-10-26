import sys
import os
import streamlit as st

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from frontend.StudyBuddy import level
from frontend.utils.api_client import similar_quiz

st.title("🔀 Generate Similar Questions")
st.write(
    "Want to practice a concept from different angles? Upload a question, and "
    "I'll generate similar ones for you."
)

question_file = st.file_uploader("Upload a question here", type=["pdf", "docx", "txt"])

if st.button("Generate Similar Questions"):
    if not question_file:
        st.warning("Please upload a question to continue.")
    elif level == "--Select Level--":
        st.warning("Please select your education level to continue.")
    else:
        with st.spinner("Creating similar questions... ✍️"):
            response = similar_quiz(question_file, level)
            st.write(response)
