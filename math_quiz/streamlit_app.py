from PIL import Image
from pathlib import Path
from st_cookies_manager import EncryptedCookieManager

import alog
import streamlit as st
import uuid

from math_quiz.prompts import random_prompt

im = Image.open(Path("./math_quiz/favicon.ico").resolve())

st.set_page_config(
    page_title="Math Quiz",
    page_icon=im,
    initial_sidebar_state="collapsed"
)

cookies = EncryptedCookieManager(
    prefix='mq_',
    password='exDzQsF+pxrHKVQV'
)


def get_session_id():
    api_key = str(uuid.uuid4())
    return api_key


def wait_for_cookies():
    if not cookies.ready():
        st.stop()


if 'sessions' not in st.session_state:
    st.session_state['sessions'] = dict()

session_id = get_session_id()

if session_id not in st.session_state['sessions']:
    st.session_state['sessions'][session_id] = dict()
    st.session_state['sessions'][session_id]['messages'] = []

if st.sidebar.button("Clear conversation history"):
    alog.info('### clear conversation ###')
    st.sidebar.success("Conversation history cleared")

cookies.save()
wait_for_cookies()

alog.info('\n#### all good ####')
messages=[]
if 'messages' not in st.session_state:
    st.session_state['messages']=messages
    messages.append(random_prompt())

messages = st.session_state['messages']
chat_container = st.empty()

def render_chat():
    with chat_container.container():
        alog.info(len(messages))
        for msg in messages:
            if 'question' in msg:
                with st.chat_message('assistant'):
                    question = msg["question"]
                    result = f':green[{question}]'
                    alog.info('### render ###')
                    st.write(result)
            if 'response' in msg:
                with st.chat_message('user'):
                    question = msg["response"]
                    result = f':green[{question}]'
                    alog.info('### render ###')
                    st.write(result)

render_chat()

prompt = st.chat_input("Say something")
if prompt:
    messages.append(dict(response = prompt))
    render_chat()