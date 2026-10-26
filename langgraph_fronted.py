from langgraph import chatbot
from langchain_core.messages import HumanMessage
import streamlit as st

#config
CONFIG = {'configurable':{'thread_id':'thread_id'}}

# st.season_state
if "massage_history" not in st.session_state:
    st.session_state['message_history'] = []

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input("Type Here..")

if user_input:

    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.text(user_input)


    response = chatbot.invoke({'messages':{HumanMessage(content=user_input)}},config=CONFIG)
    ai_message = response['messages'][-1].content
    with st.session_state['message_history'].append({'role':'assistant','content':response}):
        st.text(ai_message)
    

