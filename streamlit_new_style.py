import streamlit as st
from streamlit_chat import message
import requests

# Custom CSS for styling the chat interface
st.markdown("""
    <style>
    .chatbox {
        max-height: 400px;
        overflow-y: auto;
        display: flex;
        flex-direction: column;
    }
    .user-message, .bot-message {
        display: flex;
        align-items: flex-end;
        padding: 10px;
        margin: 5px;
        border-radius: 15px;
    }
    .user-message {
        background-color: #d1e7dd;
        text-align: right;
        align-self: flex-end;
        color: #0d6efd;
    }
    .bot-message {
        background-color: #f8d7da;
        text-align: left;
        align-self: flex-start;
        color: #842029;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Chatbot")

if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

def get_bot_response(user_input):
    response = requests.post('http://127.0.0.1:5000/api/chat', json={'message': user_input})
    if response.status_code == 200:
        return response.json().get('response', 'No response from the bot.')
    else:
        return 'Failed to get response from the chatbot API'

user_input = st.text_input("You:", key="input")

if st.button('Send'):
    if user_input:
        bot_response = get_bot_response(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(bot_response)
    else:
        st.warning('Please enter a message to send.')

st.markdown("<div class='chatbox'>", unsafe_allow_html=True)
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])):
        st.markdown(f"<div class='user-message'>{st.session_state['past'][i]}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='bot-message'>{st.session_state['generated'][i]}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
