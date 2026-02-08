# Personal Project
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