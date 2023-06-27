import streamlit as st
import page1, page2, page3, page4


PAGES = {
    "How to use your AI notes?": page1,
    "Chapter 1: What are LLMs?": page2,
    "Chapter 2: What is Langchain?": page3,
    "Experiments": page4

}

st.sidebar.title('AI-Powered Notes')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

