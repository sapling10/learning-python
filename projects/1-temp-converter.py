# basic converter between F to C or F to C
# takes in user input for conversion type,
# than the current temperature
def main():
    # get what conversion they want to make
    type = input("Convert to F or C?: ")
    while ((type != "C") and (type != "c") and (type != "F") and (type != "f")):
        print(f"{type} is not a valid input, use F or C...")
        type = input("Convert to F or C?: ")
    # we have a correct input, get value
    while True:
        try:
            value = float(input("What is your current temperature?: "))
            break
        except:
            print("not a valid type, try again...")
    # convert
    if ((type == "C") or (type == "c")):
        print(f"converting F -> C...")
        conversion = (value - 32) * 5/9
        print(f"{value}F -> {round(conversion, 4)}C")
    else:
        print(f"converting C -> F...")
        conversion = (value * 9/5) + 32
        print(f"{value}C -> {round(conversion, 4)}F")

if __name__ == "__main__":
    main()
