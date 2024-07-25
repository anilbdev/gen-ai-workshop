# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route('/api/message', methods=['GET'])
# def get_message():
#     return jsonify({'message': 'from api'})

# @app.route('/api/greeting/<name>', methods=['GET'])
# def get_greeting(name):
#     return jsonify({'greeting': f'Hello, {name}!'})

# @app.route('/api/square/<int:number>', methods=['GET'])
# def get_square(number):
#     return jsonify({'square': number ** 2})

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify
import os
from openai import AzureOpenAI

app = Flask(__name__)

predefined_answers = {
    "hello": "Hi there!",
    "how are you": "I'm a bot, but I'm doing great! How can I assist you today?",
    "bye": "Goodbye! Have a great day!"
}

endpoint = os.getenv("ENDPOINT_URL", "-----------")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-35-turbo")
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key='********',
    api_version="2024-05-01-preview",
)
  

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').lower()
    # response = predefined_answers.get(user_message, "Sorry, I don't understand that.")

    completion = client.chat.completions.create(
    model=deployment,
    messages= [
    {
      "role": "user",
      "content": user_message
    }],
    max_tokens=800,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False
    )
    print(completion)
    print(completion.choices[0].message.content)
    return jsonify({'response': completion.choices[0].message.content})

if __name__ == '__main__':
    app.run(debug=True)






      
    

print(completion.to_json())
