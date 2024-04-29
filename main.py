"""
streamlit run E:\learninglangchain\pythonProject\frontend\app.py [ARGUMENTS]
"""

from backend.core import run_llm
import streamlit as st

from streamlit_chat import message

st.header(" Document Helper Bot !! ")

prompt = st.text_input("Prompt", placeholder="Enter your query here....")

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []

if "chat_answer_history" not in st.session_state:
    st.session_state["chat_answer_history"] = []

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

if prompt:
    with st.spinner("Generating Response..."):
        generated_response = run_llm(query=prompt, chat_history=st.session_state['chat_history'])
        formatted_response = f'{generated_response["answer"]} \n'

    st.session_state['user_prompt_history'].append(prompt)
    st.session_state['chat_answer_history'].append(formatted_response)
    st.session_state['chat_history'].append((prompt, generated_response["answer"]))

if st.session_state['chat_answer_history']:
    for generated_response, user_query in zip(st.session_state['chat_answer_history'], st.session_state['user_prompt_history']):
        message(user_query, is_user=True)
        message(generated_response)






