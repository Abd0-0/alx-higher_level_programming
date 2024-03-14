#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ac = len(sys.argv) - 1
    av = sys.argv
    if ac == 0:
        print("0 arguments")
    elif ac == 1:
        print("1 argument")
    else:
        print(f"{ac} arguments")
    for i in range(1, ac + 1):
        print(f"{i}: {av[i]}")
