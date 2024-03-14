#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    av = sys.argv
    ac = len(av)
    s = 0
    for i in range(1, ac):
        s += int(av[i])
    print(s)
