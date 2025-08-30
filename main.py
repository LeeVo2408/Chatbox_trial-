from langchain_ollama.llms import OllamaLLM;
from langchain_core.prompts import ChatPromptTemplate;
import streamlit as st
import time 

from core.vector import retriever
from components.sidebar import sidebar
from Ui import stream_data

def main():

    #call the streamlit setup function to initialize the page

    model = OllamaLLM(model="llama3.2")  
    template = """
    You are an exeprt in answering questions about a pizza restaurant

    Here are some relevant reviews: {reviews}

    Here is the question to answer: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    # Remove: chain = model | prompt

    st.set_page_config(page_title="Pizza Restaurant Chatbot", layout="wide", initial_sidebar_state="collapsed", page_icon=":pizza:")
    st.title("🍕 Pizza Restaurant Chatbot")
    st.header("Ask me anything about the pizza restaurant reviews!")

    sidebar()
    
    user_input = st.chat_input("Ask a question about the pizza restaurant reviews:")
    
    if user_input:
        with st.spinner('Generating response...'):
            reviews = retriever.invoke(user_input)
            # Format the prompt with your variables
            formatted_prompt = prompt.format(reviews=reviews, question=user_input)
            # Pass the formatted prompt (string) to the model
            response = model.invoke(formatted_prompt)
            time.sleep(0.5) 
            
        st.success('Response generated!')
        st.write("**Response:**")
        st.write(stream_data(response))




if __name__ == "__main__":
    main()