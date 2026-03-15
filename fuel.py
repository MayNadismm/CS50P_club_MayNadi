while True:
    try:
        x,y = int(input("Enter x: ")), int(input("Enter y: "))
    except (ValueError):
        print("Enter integers only.")
        continue
    if y == 0:
        print("y cannot be zero.")
        continue
    elif x > y:
        print("x cannot be greater than y.")
        continue
    elif x < 0 or y <= 0:
        print("x and y cannot be negative.")
        continue
    break

percentage = (x / y) * 100
if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage:.0f}%")