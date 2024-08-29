import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    (r'Hi|Hello|Hey', ['Hello! How can I assist you today?', 'Hi there!']),
    (r'What is your name?', ['I am a simple chatbot created to help you.']),
    (r'How are you?', ['I am just a computer program, but I am doing well!']),
    (r'What can you do?', ['I can answer a few predefined questions. Try asking me something!']),
    (r'Quit|Bye|Exit', ['Goodbye! Have a nice day!']),
    (r'(.*)', ['I am not sure how to respond to that. Can you ask something else?'])
]

def chatbot():
    # Create a chatbot instance with the defined patterns and responses
    chat = Chat(pairs, reflections)
    
    print("Hello! I am your chatbot. Type 'Quit', 'Bye', or 'Exit' to end the conversation.")
    
    # Start the conversation
    while True:
        user_input = input("Enter your Question : ")
        response = chat.respond(user_input)
        print("Chatbot:", response)
        if user_input.lower() in ['quit', 'bye', 'exit']:
            break

if __name__ == "__main__":
    chatbot()
