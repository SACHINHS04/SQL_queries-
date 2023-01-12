import openai

import streamlit as st

def get_api_key():

    api_key = st.text_input("Enter your OpenAI API key:")

    if api_key:

        openai.api_key = api_key

        return True

    else:

        st.error("API key is required.")

        return False

def generate_query():

    query_input = st.text_input("Enter a description of the query you want to create:")

    prompt = (f"Write a SQL query to {query_input}")

    completions = openai.Completion.create(

        engine="text-davinci-002",

        prompt=prompt,

        max_tokens=1024,

        n=1,

        stop=None,

        temperature=0.5,

    )

    message = completions.choices[0].text

    st.success(f"SQL query: {message}")

# Streamlit app

st.set_page_config(page_title="SQL Query Generator", page_icon=":guardsman:", layout="wide")

st.title("SQL Query Generator")

if get_api_key():

    generate_query()
