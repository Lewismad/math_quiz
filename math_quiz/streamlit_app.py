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
        for msg in messages:
            if 'question' in msg:
                with st.chat_message('assistant'):
                    question = msg["question"]
                    result = f':green[{question}]'
                    # alog.info('### render ###')
                    st.write(result)
            if 'response' in msg:
                with st.chat_message('user'):
                    score=calc_overall(messages)
                    score=round(score*100)
                    question = msg["response"]
                    if msg['is_correct']:
                        result = f':green[{question} :heavy_check_mark:]'
                    else:
                        result = f':red[{question} :heavy_multiplication_x:]'

                    result += f'{score}%'
                    # alog.info('### render ###')
                    st.write(result)
def calc_overall(messages):
    user_messages=[msg for msg in messages
                   if 'response' in msg]
    correct_msgs=[msg for msg in user_messages
                  if msg['is_correct']]
    return len(correct_msgs)/len(user_messages)

render_chat()

prompt = st.chat_input("Say something")
if prompt:
    num_response = None

    try:
        num_response=int(prompt)
        last_msg=messages[-1]

        result = last_msg['a'] * last_msg['b']
        messages.append(dict(
            response=prompt,
            is_correct=result == num_response
        ))

        render_chat()
    except Exception as err:
        st.error(str('Use numbers only.'))

    messages.append(random_prompt())
    render_chat()
    alog.info(calc_overall(messages))