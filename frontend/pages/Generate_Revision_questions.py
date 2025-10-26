import sys
import os
import streamlit as st

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from frontend.StudyBuddy import level
from frontend.utils.api_client import generate_questions

st.title("🧠 Generate Custom Revision Questions")
st.write(
    "Ready to test your knowledge? Upload your lecture and past paper files to "
    "generate a personalized quiz."
)
lecture_file = st.file_uploader(
    "Upload your lecture notes", type=["pdf", "docx", "txt"]
)
pastpaper_file = st.file_uploader("Upload a past paper", type=["pdf", "docx", "txt"])

if st.button("Generate Questions"):
    if not lecture_file:
        st.warning("Please upload your lecture notes to continue.")
    elif not pastpaper_file:
        st.warning("Please upload a past paper to continue.")
    elif level == "--Select Level--":
        st.warning("Please select your education level to continue.")
    else:
        with st.spinner("Brewing your questions... 🧑‍🍳"):
            response = generate_questions(lecture_file, pastpaper_file, level)
            st.write(response)
