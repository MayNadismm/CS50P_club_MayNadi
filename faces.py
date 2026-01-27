def convert(key):
    emoji = ""
    if key == ":)":
        emoji = "🙂"
    elif key == ":(":
        emoji = "🙁"
    return emoji

#print(convert(":)"))

def main():
    global text
    modified_text = ""
    emoticon = ""
    char = 0
    while char < len(text):
        if text[char] == ":":
            emoticon = text[char] + text[char+1]
            modified_text += convert(emoticon)
            char += 2
        else:
            modified_text += text[char]
            char += 1
    print(modified_text)
    """
    for word in text:
        if word == ":)" or word == ":(":
            modified_text += convert(word)
        else:
            modified_text += word
    print(modified_text)
"""
text = ""
text = input("Enter the text: ")
main()

