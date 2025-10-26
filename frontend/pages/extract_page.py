import sys
import os
import streamlit as st

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from frontend.utils.api_client import upload_and_extract
from frontend.main import level
st.title("🎯 Extract Key Study Topics")
st.write(
    "Upload your lecture notes and a past paper, and I'll identify the most "
    "important topics for you to focus on."
)

lecture_file = st.file_uploader(
    "Upload your lecture notes", type=["pdf", "docx", "txt"]
)
pastpaper_file = st.file_uploader("Upload a past paper", type=["pdf", "docx", "txt"])

if st.button("Extract Topics"):
    if not lecture_file:
        st.warning("Please upload your lecture notes to continue.")
    elif not pastpaper_file:
        st.warning("Please upload a past paper to continue.")
    elif level == "--Select Level--":
        st.warning("Please select your education level to continue.")
    else:
        with st.spinner("Analyzing your files... 🧐"):
            response = upload_and_extract(lecture_file, pastpaper_file, level)
            st.write(response)
