#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    l = number % -10
else:
    l = number % 10
if l > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, l))
elif last_number < 6 and last_number != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, l))
else:
    print("Last digit of {} is {} and is 0".format(number, l))
