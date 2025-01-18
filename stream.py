import os
import pandas as pd
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# Load the database
DB_FILE = "users_with_chatlogs.csv"
df = pd.read_csv(DB_FILE)

# Streamlit page configuration
st.set_page_config(page_title="AI Chatbot with Database", page_icon="🤖")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat messages from history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to query the database
def query_database(user_input):
    user_keywords = user_input.lower().split()
    
    # Check if the user is requesting chat history
    if "chat history" in user_input.lower():
        user_data = df[df['user_message'].str.contains('|'.join(user_keywords), case=False, na=False)]
        if not user_data.empty:
            chat_history = "\n".join(user_data['chat_response'].tolist())
            return f"Previous chat history:\n{chat_history}"
        else:
            return "No chat history found related to your request."
    
    # Search the database for relevant responses
    matched_rows = df[df['user_message'].str.contains('|'.join(user_keywords), case=False, na=False)]
    if not matched_rows.empty:
        return matched_rows.iloc[0]['chat_response']
    else:
        return "I couldn't find relevant information in the database."

# Function to generate AI response from Groq
def generate_response(user_input):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        *st.session_state.chat_history,
        {"role": "user", "content": user_input},
    ]
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.5,
        max_tokens=150,
        top_p=1,
        stream=False,
    )
    return response.choices[0].message.content

# User input
if user_input := st.chat_input("Type your message here..."):
    # Display user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Determine if query is for the database or general chat
    if "database" in user_input.lower() or "chat history" in user_input.lower():
        db_response = query_database(user_input)
        st.session_state.chat_history.append({"role": "assistant", "content": db_response})
        with st.chat_message("assistant"):
            st.markdown(db_response)
    else:
        ai_response = generate_response(user_input)
        st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
        with st.chat_message("assistant"):
            st.markdown(ai_response)
