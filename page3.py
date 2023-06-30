# Contents of page2.py
import streamlit as st
from ui_components import render_chapter

def app():

    json_path = 'chapters.json'
    chapter_id = 2

    render_chapter(chapter_id, json_path)
