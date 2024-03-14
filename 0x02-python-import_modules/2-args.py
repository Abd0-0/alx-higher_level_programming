#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ac = len(sys.argv) - 1
    av = sys.argv
    if ac == 0:
        print("{} arguments".format(ac))
    elif ac == 1:
        print("{} argument".format(ac))
    else:
        print("{} arguments:".format(ac))
    for i in range(1, ac + 1):
        print("{}: {}".format(i, av[i]))
