# AI_setup/streamlit_setup.py
import streamlit as st
import time

def stream_data(text: str, delay: float = 0.02):
    for word in text.split():
        yield word + " "
        time.sleep(delay)
