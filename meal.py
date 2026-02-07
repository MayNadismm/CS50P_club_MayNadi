def main(time):
    if 7 <= time <= 8:
        print("breakfast")
    elif 12 <= time <= 13:
        print("lunch")
    elif 18 <= time <= 19:
        print("dinner")

def convert(time):
    hours, minutes = time.split(":")
    minutes = int(minutes) / 60
    return float(int(hours) + minutes)

if __name__ == "__main__":
    time = input("What time is it? ")
    time = convert(time)
    main(time)