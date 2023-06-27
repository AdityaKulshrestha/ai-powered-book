import streamlit as st
from ai_components import llm_agent

# doubt_container = st.container()

# with doubt_container:
#     query = st.text_input("Enter your doubt here")
#     if query:
#         answer = llm_agent.predict(input = query)
#         st.write(answer)

# def doubt_container():
#     with st.container() as container:
#         container.write("Thanks for asking a doubt.")
#         query = container.text_input("Enter your doubt here")
#         if query:
#             answer = llm_agent.predict(input = query)
#             container.write(answer) 
#     return container


def doubt_container():
    container = st.empty()
    with container:
        st.write("This is a shared container.")
        st.text("Some shared text")
        st.text_input("Enter your doubt here")
    return container



