import random

print("Welcome from the password generator!")

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
