def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
   def is_valid(s):

    # Length must be between 2 and 6
    if not (2 <= len(s) <= 6):
        return False

    # First two must be letters
    if not s[:2].isalpha():
        return False

    # Last two must be digits
    if not s[-2:].isdigit():
        return False

    # No special characters allowed
    if not s.isalnum():
        return False

    return True

main()