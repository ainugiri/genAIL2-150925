def chat():
    print("Welcome to the Rule-Based ChatBot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":    
            print("Goodbye!")
            break
        elif user_input in ["hi", "hello", "hey"]:
            print("ChatBot: Hello! How can I assist you today?")
        elif user_input in ["iphone", ["service", "support"]]:
            if user_input == "iphone":
                print("ChatBot: You mentioned iPhone. How can I help you with it?")
                print("ENter the model ")
                model = int(input())
                if model == 14:
                    print("ChatBot: iPhone 14 is the latest model with advanced features.")
                elif model == 13:
                    print("ChatBot: iPhone 13 has a great camera and performance.")
                elif model == 12:
                    print("ChatBot: iPhone 12 is known for its OLED display and 5G support.")
        elif user_input == "how are you?":
            print("ChatBot: I'm just a program, but thanks for asking!")
        else:
            print("ChatBot: I'm sorry, I don't understand that.")

chat()