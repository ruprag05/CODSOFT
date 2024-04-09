import random

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if user_input in ["hi", "hello", "hey", "hola"]:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but thanks for asking!"
    elif "your name" in user_input:
        return "I'm just a humble chatbot. What's your name?"
    elif "my name is" in user_input:
        name = user_input.split("is")[-1].strip()
        return f"Nice to meet you, {name}!"
    else:
        return "I'm sorry, I don't understand. Can you please rephrase or ask something else?"

def main():
    print("Welcome! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        else:
            response = chatbot_response(user_input)
            print("Bot:", response)

if __name__ == "__main__":
    main()
