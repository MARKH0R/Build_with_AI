import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini Pro model
model = genai.GenerativeModel("gemini-pro")

# Start the chat with an empty history
chat_history = []
chat = model.start_chat(history=chat_history)

def get_gemini_response(question):
    """Sends a question to Gemini Pro, appends the conversation to history,
       and returns the response."""
    global chat_history  # Access the global chat_history variable
    chat_history.append({"role": "user", "content": question})
    response = chat.send_message(question, stream=True)
    chat_history.extend([{"role": "assistant", "content": chunk.text} for chunk in response])
    return response

# Enable continuous conversation with history preservation
while True:
    question = input("Enter your question (or type 'quit' to exit): ")
    if question.lower() == "quit":
        break
    response = get_gemini_response(question)
    print("Response:")
    for chunk in response:
        print(chunk.text)
