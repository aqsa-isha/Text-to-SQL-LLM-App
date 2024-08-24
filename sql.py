from dotenv import load_dotenv
load_dotenv()  # load all the environment variables
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load the Google Gemini Model and provide queries as a response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    # Combine the prompt and question into a single string
    content = f"{prompt}\n\n{question}"
    response = model.generate_content(content)
    return response.text

# Function to retrieve query results from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return rows

# Define the prompt as a single string
prompt = """
You are an expert in converting English questions to SQL query!
The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION.

For example,
Example 1 - How many entries of records are present?,
the SQL command will be something like this: SELECT COUNT(*) FROM STUDENT;

Example 2 - Tell me all the students studying in Data Science class?,
the SQL command will be something like this: SELECT * FROM STUDENT WHERE CLASS="Data Science";
also the SQL code should not have ``` in beginning or end and sql word in output.
"""

# Streamlit App
st.set_page_config(page_title="I can retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    st.write("Generated SQL Query:", response)  # Display the generated SQL query
    try:
        data = read_sql_query(response, "student.db")
        st.subheader("The response is:")
        for row in data:
            st.write(row)
    except Exception as e:
        st.error(f"Error executing the query: {e}")
