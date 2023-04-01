def main():
    # all basic operators... +, -, *, /, %, 
    # but there is also ** for exponent, and // for floor division

    # all basic comparison operators... ==, !=, >, <, >=, <=

    # all basic assignment operators... ==, +=, -=, *=, /=, %=, **=, //=
    
    # all basic bitwise operators... &, |, ^, ~, <<, >>

    # all basic logical operators... and, or, not, in, not in, is, is not
    
    print("While:")
    x = 0
    while (x < 10):
        print(f"\tin while loop... x = {x}")
        x = x + 1
    
    print("For:")
    print("\tusing in...")
    for number in range(0, 9):
        print(f"\tin for loop... number = {number}")
    
    print("\n\tusing range...")
    s = "Hello World"
    for idx in range(len(s)):
        print(f"\tin for loop... index = {idx}, current letter = {s[idx]}")

if __name__ == "__main__":
    main()
