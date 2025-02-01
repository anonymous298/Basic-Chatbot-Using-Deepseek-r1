from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import streamlit as st


st.title('Chatbot Using Open-Source Deepseek-r1-1.5b With Ollama')
user_input = st.text_input('What You Want To Search?')

prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are an Intelliegent Assistant'),
        ('user', 'Question: {input}')
    ]
)

llm = Ollama(model='deepseek-r1:1.5b')

chain = prompt | llm | StrOutputParser()

if st.button('Ask'):
    response = chain.invoke({'input' : user_input})
    st.write(response)

