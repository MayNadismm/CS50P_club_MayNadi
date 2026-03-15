# Personal Project
frequency = int(input("How many times do you wanna play?: "))
your_score = []
computer_score = []
while frequency > 0:
    def match(userChoice, comChoice):
        if userChoice == comChoice :
            return "It's a tie!"
        elif (userChoice == "rock" and comChoice == "scissors") or \
            (userChoice == "scissors" and comChoice == "paper") or \
            (userChoice == "paper" and comChoice == "rock"):
            return "You win!"
        else:
            return "Computer wins!"
    import random

    choices = input("Enter your choice (rock, paper, scissors): ").lower()
    comChoice = random.choice(["rock", "paper", "scissors"])
    result = match(choices, comChoice)
    print(f"{result} Computer chose {comChoice}")
    frequency -= 1
    if result == "You win!":
        your_score.append(1)
    elif result == "Computer wins!":
        computer_score.append(1)

print("-"*30)
if len(your_score) > len(computer_score):
    print("Congratulations, you won the game! \nYou're to get a generated password of your own!")
    password = ""
    name = input("Please enter your name: ")
    number = input("Enter your favourite number(2 digits): ")
    freq = len(name)
    while freq < 5: #concentrating the name with its first letter until the length of the name is 5
        name += name[0]
        freq += 1

    password = name + number

    password = list(password) #Change the password to a list
    random.shuffle(password) #Shuffle the password
    shuffled_password = "".join(password)
    print(shuffled_password)

elif len(your_score) < len(computer_score):
    print("Computer won the game!")
else:
    print("It's a tie game!")

"""
# Personal Project 1 (Match Function Practice)
score = int(input("Enter your score (0-100): "))
match score:
    case s if 90 <= s <= 100:
        grade = 'A'
    case s if 80 <= s < 90:
        grade = 'B'
    case s if 70 <= s < 80:
        grade = 'C'
    case s if 60 <= s < 70:
        grade = 'D'
    case s if 50 <= s < 60:
        grade = 'F'
    case _:
        grade = 'You got what?'
print(f"Your grade is: {grade}")    
"""