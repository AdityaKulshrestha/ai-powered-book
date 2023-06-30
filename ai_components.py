import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.0)
memory = ConversationBufferMemory()


def respond_to_query(query):
    llm_agent = ConversationChain(
        llm=llm,
        memory=memory,
    )
    return llm_agent.run(query)


def create_ques_ans():
    '''Function to create new questions everytime for the users!'''
    prompt = """Prepare a list of 10 multiple choice question in the form of the three python lists. The first list 
    should contain all the questions, the second list contain options that means for each questions 4 options and 
    last list should contain all correct answers to the questions. The list should questions from streamlit and 
    python programming basics. The three lists should be within a bigger list. Terminate all the non-terminated string literal 
    at appropriate places in python"""
    # prompt = PromptTemplate.from_template(prompt)
    # prompt.format(product="colorful socks")
    # chain = LLMChain(llm=llm, prompt=prompt)
    llm = OpenAI(temperature=0.9)
    return llm.predict(prompt)
