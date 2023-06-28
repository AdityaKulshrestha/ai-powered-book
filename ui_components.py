import json
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


# Define the function
def render_chapter(chapter_id, json_path):
    # Load the JSON data
    with open(json_path, 'r') as f:
        data = json.load(f)

    # Traverse each chapter in the data
    for chapter in data['chapters']:
        # Check if the chapter's id is the id that we're looking for
        if chapter['chapterId'] == chapter_id:
            # Display the chapter title
            st.title(chapter['chapterTitle'])
            
            # Display each section of the chapter
            for section in chapter['sections']:
                st.header(section['sectionTitle'])
                if 'content' in section:
                    st.markdown(section['content'])
                if 'code' in section:
                    st.code(section['code'])

                # Display each subsection of the chapter
                if 'subsections' in section:
                    for subsection in section['subsections']:
                        st.subheader(subsection['subsectionTitle'])
                        if 'content' in subsection:
                            st.markdown('*' + subsection['content'] + '*')  # Wrapping the content inside asterisks will italicize the text in markdown
                        if 'code' in subsection:
                            st.code(subsection['code']) 
