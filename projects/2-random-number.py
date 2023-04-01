# gets the low and high range from user, generates random number
# in that range

import random

def getUserInput():
    while True:
        try:
            lowRange = int(input("Enter the lower range: "))
            break
        except:
            print("Incorrect value...")
    while True:
        try:
            highRange = int(input("Enter the higher range: "))
            break
        except:
            print("Incorrect value...")
    return [lowRange, highRange]

def main():
    range = getUserInput()
    while (range[0] > range[1]):
        print("Low range cannot be > high range...")
        range = getUserInput()

    rand = random.randint(range[0], range[1])
    print(f"Your random number is {rand}")

if __name__ == "__main__":
    main()
