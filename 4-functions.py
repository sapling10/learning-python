def printIt(s):
    print(s)
    return

def changeList(l):
    l = [4, 5, 6]
    return

def changeListReturn():
    l = [4, 5, 6]
    return l

def appendList(l):
    l.append([7, 8, 9])
    return

def main():
    x = "Hello World (but with a function)\n"
    printIt(x)

    print("all functions are based by reference, here is a test")
    l = [1, 2, 3]
    print(f"\tl = {l}")
    changeList(l)
    print(f"\tcalled function changeList...\n\tl = {l}")
    l = changeListReturn()
    print(f"\tcalled function changeListReturn...\n\tl = {l}")
    appendList(l)
    print(f"\tcalled function appendList...\n\tl = {l}")


if __name__ == "__main__":
    main()
