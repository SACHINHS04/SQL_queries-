import os
import openai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()





api_key = os.environ.get("OPENAI_API_KEY")

def generate_query():
    # Get API key from environment variable
    #api_key = os.environ.get("OPENAI_API_KEY")
   # openai.api_key = api_key

    # Get user input
    query_input = st.text_input("Enter a description of the query you want to create:")
    
    # Use OpenAI to generate SQL query
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
generate_query()
