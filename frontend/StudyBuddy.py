import streamlit as st

st.set_page_config(page_title="Classroom AI", layout="wide")

st.markdown("<h1 style='text-align: center;'>Classroom AI🎓</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>🎓 Welcome to Your AI-Powered Classroom Assistant</h2>", unsafe_allow_html=True)
st.write(
    "Your personal AI tutor, ready to help you excel in your studies. "
    "Select your education level to unlock the features."
)

level = st.selectbox(
    "Please select your education level to get started:",
    [
        "-- Select Level --",
        "Lower Primary (Grade 1-5)",
        "Upper Primary (Grade 6-9)",
        "High School (Grade 10-12)",
        "College/University",
    ],
)

if level != "-- Select Level --":
    st.session_state["level"] = level
    st.success(f"Great! You've selected {level}. Here are the tools available for you:")

    st.page_link("pages/AI_Powered_Analysis.py", label="🎯 Extract Key Study Topics", icon="🎯")
    st.page_link(
        "pages/Generate_Revision_questions.py",
        label="🧠 Generate Custom Revision Questions",
        icon="🧠",
    )
    st.page_link(
        "pages/Simplify_Explanation.py",
        label="💡 Simplify Complex Explanations",
        icon="💡",
    )
    st.page_link("pages/AI_Marking.py", label="📝 Get Your Work Marked", icon="📝")
    st.page_link(
        "pages/Generate_Similar_Questions.py",
        label="🔀 Generate Similar Questions",
        icon="🔀",
    )
