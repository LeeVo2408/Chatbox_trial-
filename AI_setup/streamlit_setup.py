# AI_setup/streamlit_setup.py
import streamlit as st
import time

def init_page() -> None:
    st.set_page_config(
        page_title="Pizza Restaurant Chatbot",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    st.title("Pizza Restaurant Review Chatbot")
    st.header("Ask me anything about the pizza restaurant reviews!")

def get_user_input() -> str | None:
    # render every run, return the latest message (or None)
    return st.chat_input("Ask a question about the pizza restaurant reviews:")

def stream_data(text: str, delay: float = 0.02):
    for word in text.split():
        yield word + " "
        time.sleep(delay)
