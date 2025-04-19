import streamlit as st
import requests
import pandas as pd


st.set_page_config(
    page_title="SHL Assessment Recommendation System",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="auto"
)


st.markdown(
    """
    <style>
    body {
        background-color: #0e1117;
        color: #fafafa;
    }
    .stMarkdown table {
        font-size: 18px;
        color: #fafafa;
    }
    .stMarkdown td, .stMarkdown th {
        padding: 8px;
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        font-size: 18px;
    }
    .stButton>button {
        font-size: 18px;
    }
    /* Sidebar profile styling */
    .sidebar-content p {
        font-size: 32px;
        color: #fafafa;
        text-align: center;
        line-height: 1.4;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.sidebar.markdown(
    "<p><strong>Lakshay Trehan</strong><br>"
    "B.Tech CS Undergraduate at Indraprastha Institute of Information Technology Delhi (IIITD'2026)<br>"
    "Passionate Software Engineer 🚀 | Web Developer 💻<br>"
    "LLM Enthusiast 🤖 | AI & ML 🧠</p>",
    unsafe_allow_html=True
)


st.title("🔍 SHL Assessment Recommendation System")


query = st.text_area("Enter Job Description or Query:")


if st.button("Get Recommendations"):
    if not query:
        st.warning("Please enter a query!")
    else:
        try:
            res = requests.post(
                "http://localhost:8000/recommend", json={"query": query}
            )
            assessments = res.json().get("recommended_assessments", [])

            if not assessments:
                st.warning("No recommendations found.")
            else:
                for a in assessments:
                    metadata = a.get("metadata", {})
                    content = a.get("page_content", "No content available.")

                    name = metadata.get("name", "Unnamed Assessment")
                    url = metadata.get("url", "#")
                    description = metadata.get("description", content)
                    remote_support = metadata.get("remote_support", "N/A")
                    adaptive_support = metadata.get("adaptive_support", "N/A")
                    duration = metadata.get("duration", "N/A")
                    test_type = metadata.get("test_type", "N/A")

                    
                    st.markdown(f"### [**{name}**]({url})")
                    st.write(description)

                    
                    df = pd.DataFrame({
                        "Remote Support": [remote_support],
                        "Adaptive Support": [adaptive_support],
                        "Duration (mins)": [duration],
                        "Type": [test_type]
                    })
                    st.table(df)
                    st.markdown("---")

        except Exception as e:
            st.error(f"An error occurred: {e}")