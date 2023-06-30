import streamlit as st
from ui_components import doubt_container, render_chapter

def app():
    # st.title("Overview of Tech Stack")
    json_file = 'chapters.json'
    chapter_id = 3

    render_chapter(chapter_id, json_file)







    