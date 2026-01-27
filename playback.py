text = input("Enter the text: ")
modified_text = ""
for char in text:
    if char == " ":
        modified_text += "..."
    else:
        modified_text += char
print(modified_text)
#method 2
text = text.replace(" ", "...")
print(text)
