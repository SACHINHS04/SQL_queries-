import openai
import streamlit as st

def generate_query():
    # Get API key from user
    api_key = st.text_input("Enter your OpenAI API key:")
    openai.api_key = api_key

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
