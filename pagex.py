import streamlit as st
from ai_components import llm_agent
from ui_components import doubt_container

def app():
    st.title("My experiments")

    st.header("Ask a doubt.")

    # query = st.text_input("Enter your doubt here")

    # if query:
    #     answer = llm_agent.predict(input = query)
    #     st.write(answer)

    st.write("Large language models learn from huge volumes of data. As its name suggests, central to an LLM is the size of the dataset it’s trained on. But the definition of “large” is growing, along with AI.")
    ask_doubt = st.button("Ask a doubt")

    if ask_doubt:
        doubt_container()






    