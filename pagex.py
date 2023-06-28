
import streamlit as st
from ai_components import llm_agent
from ui_components import doubt_container, render_chapter


def app():
    json_path = "chapters.json"

    # Your desired chapter id
    chapter_id = 1

    render_chapter(chapter_id, json_path)

    # st.write("Large language models learn from huge volumes of data. As its name suggests, central to an LLM is the size of the dataset it’s trained on. But the definition of “large” is growing, along with AI.")
    # ask_doubt = st.button("Ask a doubt")

    # if ask_doubt:
    #     doubt_container()








    