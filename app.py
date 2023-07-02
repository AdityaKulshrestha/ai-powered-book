import streamlit as st
from ui_components import doubt_container
import page1, page2, page3, page4, page5, page6
import os

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

PAGES = {
    "How to use your AI notes?": [page1, '1'],
    "Chapter 1: What are LLMs?": [page2, '2'],
    "Chapter 2: What is Langchain?": [page3, '3'],
    "Chapter 3 Overview of the techstack": [page4, '4'],
    "Chapter 4: Build your first AI app": [page5, '5'],
    "Chapter 5: Test your knowledge": [page6, '6']

}

st.sidebar.title('AI-Powered Notes')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection][0]
key = PAGES[selection][1]
with st.container():
    page.app()
    doubt_container(key)

st.divider()
