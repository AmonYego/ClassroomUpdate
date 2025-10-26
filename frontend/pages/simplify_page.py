import sys
import os
import streamlit as st

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from frontend.utils.api_client import simplify
from frontend.main import level
st.title("💡 Simplify Complex Explanations")
st.write(
    "Struggling with a tough concept? Upload your lecture notes, and I'll break "
    "it down for you in simple terms."
)

lecture_file = st.file_uploader(
    "Upload your lecture notes here", type=["pdf", "docx", "txt"]
)

if st.button("Simplify Explanation"):
    if not lecture_file:
        st.warning("Please upload your lecture notes to continue.")
    elif level == "--Select Level--":
        st.warning("Please select your education level to continue.")
    else:
        with st.spinner("Simplifying the explanation... 🧠"):
            response = simplify(lecture_file, level)
            st.write(response)
