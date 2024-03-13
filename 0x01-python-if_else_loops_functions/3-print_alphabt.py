#!/usr/bin/python3
for abc in range(ord('a'), ord('z') + 1):
    if abc == ord('e') or abc == ord('q'):
        pass
    else:
        print("{:c}".format(abc), end="")
