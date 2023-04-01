def main():
    # integers
    print("Integers:")
    x = 10
    y = 15
    z = x + y
    print(f"\tx = {x}\n\ty = {y}\n\tz = x + y = {z}")
    print(f"\tx, y, and z are {type(x)}\n")

    # floats
    print("Floats:")
    x = 12.5
    y = 32.25
    z = x + y
    print(f"\tx = {x}\n\ty = {y}\n\tz = x + y = {z}")
    print(f"\tx, y, and z are {type(x)}\n")

    # strings
    print("Strings:")
    x = "hello"
    y = "world"
    z = x + " " + y
    print(f"\tx = {x}\n\ty = {y}\n\tz = x + (space) + y = {z}")
    print(f"\tx, y, and z are {type(x)}\n")

    # lists
    print("Lists:")
    l = ["abcd", 123, 4.567]
    print(f"\tlist l = {l[0]}, {l[1]}, {l[2]}")
    print(f"\tlist l is type {type(l)}\n")

    # tuples
    print("Tuples:")
    t = ("abcd", 123, 4.567)
    print(f"\ttuple t = {t[0]}, {t[1]}, {t[2]}")
    print(f"\ttuple t is type {type(t)}")
    # important distincion
    print("\n\t*the difference between a list and a tuple is that a tuples elements cannot be changed and its size cannot change")



if __name__ == "__main__":
    main()
