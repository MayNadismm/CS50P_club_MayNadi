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
    print("Congratulations! You won the game!") 
elif len(your_score) < len(computer_score):
    print("Sorry! Computer won the game!")
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