import streamlit as st
from ui_components import render_chapter
from ai_components import respond_to_query


def app():
    tab1, tab2 = st.tabs(["Give a quick quiz!", "Work on an exciting project idea!"])
    with tab1:
        st.title("Let's test your knowledge!")
        st.header("Attempt this multiple choice based quiz and test your knowledge!")
        chapter_id = 5
        # response_list = create_ques_ans()
        # st.write(response_list)
        # response_list = eval(response_list)
        # questions_list, options, answers = [eval(value) for value in response_list]
        # st.write(questions_list, options, answers)
        questions_list = {"questions": [
            "What is Streamlit?",
            "What is Python used for?",
            "What is the output of print(2 + 3 * 4)?",
            "What is the correct syntax to create a function in Python?",
            "What is the output of 'Hello'[1:]?",
            "Which data type is mutable in Python?",
            "What is the purpose of the 'if' statement in Python?",
            "What is the output of 'Python'[::-1]?",
            "Which of the following is not a valid Python variable name?",
            "What is the purpose of the 'for' loop in Python?"
        ],
            "options": [
                ["A framework for building web applications", "A programming language", "A data visualization library",
                 "A database management system"],
                ["Web development", "Machine learning", "Data analysis", "All of the above"],
                ["14", "15", "20", "23"],
                ["def my_function():", "create function my_function():", "my_function = def():",
                 "function my_function():"],
                ["ello", "Hello", "'H'", "'e'"],
                ["List", "Tuple", "String", "Dictionary"],
                ["To make decisions based on a condition", "To repeat a block of code", "To define a function",
                 "To handle exceptions"],
                ["nohtyP", "Python", "None of the above", "Syntax Error"],
                ["my-variable", "2ndVariable", "this_is_valid", "123abc"],
                ["To iterate over a sequence of elements", "To define a class", "To handle exceptions",
                 "To make decisions based on a condition"]
            ],
            "answers": ["A framework for building web applications", "All of the above", "14",
                        "def my_function():",
                        "ello", "List", "To make decisions based on a condition", "nohtyP", "123abc",
                        "To iterate over a sequence of elements"]
        }

        ans = []
        mark = 0
        with st.form(key='quiz'):
            for i, quest in enumerate(questions_list["questions"]):
                choice = st.radio('{}: {}'.format(i + 1, quest), questions_list['options'][i], key = i)
                ans.append(choice)
            submitted = st.form_submit_button("Submit")
            if submitted:
                for i, user_input in enumerate(ans):
                    print(i, user_input)
                    if questions_list["answers"][i] == user_input:
                        print("okay")
                        mark = mark + 1
            st.success("Test Score - " + str(mark))
    with tab2:
        chapter_id = 6

        json_path = 'chapters.json'
        render_chapter(chapter_id, json_path)
        st.subheader(respond_to_query("""Suggest a nice project idea on building an application using streamlit and openai. "
                                   The idea should be very specific and very very simple for beginners. 
                                   Suggest something as simple as a daily good motivational thought creator.
                                   Give the suggestion in one or two lines."""))
