#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
if number < 0:
    ln = number % -10
else:
    ln = number % 10
if ln > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, ln))
elif ln < 6 and ln != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(n, ln))
else:
    print("Last digit of {} is {} and is 0".format(number, ln))
