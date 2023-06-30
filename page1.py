import streamlit as st
from ui_components import render_chapter

def app():
    json_file = 'chapters.json'
    chapter_id = 0
    render_chapter(chapter_id, json_file)

