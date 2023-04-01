def main():
    # integers (signed)
    print("Integers:")
    x = 10
    y = 15
    z = x + y
    print(f"\tx = {x}\n\ty = {y}\n\tz = x + y = {z}")
    print(f"\tx, y, and z are {type(x)}\n")

    # complex
    print("Complex:")
    x = 2+3j
    y = 5+2j
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
        # can be sliced...
        # z[0]   is the first character
        # z[2:5] is the 3rd character to the 5th
        # z[2:]  is the 3rd character to the end
    print("Strings:")
    x = "hello"
    y = "world"
    z = x + " " + y
    print(f"\tx = {x}\n\ty = {y}\n\tz = x + (space) + y = {z}")
    print(f"\tx, y, and z are {type(x)}\n")

    # bools
    print("Booleans:")
    x = True
    y = False
    print(f"\tx = {x}\n\ty = {y}")
    print(f"\tx and y are {type(x)}\n")

    # lists
        # can be sliced, see strings
    print("Lists:")
    l = ["abcd", 123, 4.567]
    print(f"\tlist l = {l[0]}, {l[1]}, {l[2]}")
    print(f"\tlist l is type {type(l)}\n")

    # tuples
        # can be sliced, see strings
    print("Tuples:")
    t = ("abcd", 123, 4.567)
    print(f"\ttuple t = {t[0]}, {t[1]}, {t[2]}")
    print(f"\ttuple t is type {type(t)}")
    # important distincion
    print("\n\t*the difference between a list and a tuple is that a tuples elements cannot be changed and its size cannot change\n")

    # dictionary
        # can look for value based on key...
        # d[0] is the value at key 0
    print("Dictionary:")
    d = {"name" : "Connor", "address" : "123 1st Street", "work" : "Student"}
    print(f"\tdictionary d = {d}")
    print(f"\tdictionary d is type {type(d)}")

    # data conversion
        # int(x)        -> x to a integer
        # long(x)       -> x to a long 
        # float(x)      -> x to a floating point
        # complex(x)    -> x to a complex
        # str(x)        -> x to a string
        # repr(x)       -> x to a expression string
        # eval(str)     -> evaluates a string, returns an object
        # tuple(s)      -> s to a tuple
        # list(s)       -> s to a list
        # set(s)        -> s to a set
        # dict(s)       -> s to a dictionary
        # frozenset(s)  -> s to a frozen set
        # chr(x)        -> x (int) to a character
        # unichr(x)     -> x (int) to a unicode character
        # ord(x)        -> x (char) to an integer
        # hex(x)        -> x (int) to a hexadecimal string
        # oct(x)        -> x (int) to a octal string
    print("Data Conversion:")
    x = 10.2
    print(f"\tx = {x} and is type {type(x)}, converting to int...")
    x = int(x)
    print(f"\tx = {x} and is type {type(x)}, converting to string...")
    x = str(x)
    print(f"\tx = {x} and is type {type(x)}, converting to set...")
    x = set(x)
    print(f"\tx = {x} and is type {type(x)} (order seems to be random)")
    

if __name__ == "__main__":
    main()
