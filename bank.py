while True:
    def check(word):
        if word[0] == "h":
            if word == "hello":
                return "$0"
            else:
                return "$20"
        else:
            return "$100" 
    word = input("Enter a word: ")
    amount = check(word)
    print(f"The amount is: {amount}")
    ask = input("Do you want to continue? (yes/no): ")
    if ask.lower() != "yes":
        break
