def chatbot():
    responses = {
        "hello": "Hi!",
        "how are you": "I'm fine, thanks!",
        "bye": "Goodbye!"
    }

    print("Chatbot (type 'exit' to quit)")
    while True:
        user = input("You: ").lower()
        if user == "exit":
            print("Chatbot: Bye!")
            break
        print("Chatbot:", responses.get(user, "I don't understand..."))

if __name__ == "__main__":
    chatbot()