vowels = ['a', 'e', 'i', 'o', 'u']
the_word = input("Input: ")
def shorten(word):
    new_word = ""
    for letter in word:
        if letter not in vowels:
            new_word += letter
    return new_word
print("Output:", shorten(the_word))