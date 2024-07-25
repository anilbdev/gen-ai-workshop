# import streamlit as st
# import requests
# import plotly.express as px
# import pandas as pd

# # Welcome Text UI
# st.title("Welcome to the Enhanced Streamlit App")

# # Section for getting a message from the API
# st.header("Get Message from API")
# if st.button('Get Message'):
#     response = requests.get('http://127.0.0.1:5000/api/message')
#     if response.status_code == 200:
#         data = response.json()
#         st.success(data['message'])
#     else:
#         st.error('Failed to fetch message from API')

# # Section for getting a personalized greeting
# st.header("Get Personalized Greeting")
# name = st.text_input("Enter your name:")
# if st.button('Get Greeting'):
#     if name:
#         response = requests.get(f'http://127.0.0.1:5000/api/greeting/{name}')
#         if response.status_code == 200:
#             data = response.json()
#             st.success(data['greeting'])
#         else:
#             st.error('Failed to fetch greeting from API')
#     else:
#         st.warning('Please enter a name.')

# # Section for calculating the square of a number
# st.header("Calculate Square of a Number")
# number = st.number_input("Enter a number:", value=0)
# if st.button('Calculate Square'):
#     response = requests.get(f'http://127.0.0.1:5000/api/square/{number}')
#     if response.status_code == 200:
#         data = response.json()
#         st.success(f'The square of {number} is {data["square"]}')
#     else:
#         st.error('Failed to calculate square.')

# # Section for displaying some static information
# st.header("Static Information")
# st.markdown("""
# - **Streamlit:** A powerful tool for creating custom web apps.
# - **Flask:** A lightweight WSGI web application framework in Python.
# - **Enhanced Features:** Now with more endpoints and dynamic UI elements.
# """)

# # Section for data visualization
# st.header("Data Visualization")

# # Sample data
# data = {
#     'Category': ['A', 'B', 'C', 'D'],
#     'Values': [23, 45, 56, 78]
# }
# df = pd.DataFrame(data)

# # Bar chart
# st.subheader("Bar Chart")
# bar_chart = px.bar(df, x='Category', y='Values', title='Sample Bar Chart')
# st.plotly_chart(bar_chart)

# # Line chart
# st.subheader("Line Chart")
# line_chart = px.line(df, x='Category', y='Values', title='Sample Line Chart')
# st.plotly_chart(line_chart)


import streamlit as st
from streamlit_chat import message
import requests

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

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])):
        message(st.session_state['past'][i], is_user=True, key=f'{i}_user')
        message(st.session_state['generated'][i], key=f'{i}')

