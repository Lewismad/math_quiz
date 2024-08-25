from PIL import Image
from pathlib import Path
from st_cookies_manager import EncryptedCookieManager

import alog
import streamlit as st
import uuid

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