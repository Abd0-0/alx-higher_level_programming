#!/usr/bin/python3
def fizzbuzz():
    for n in range(1,101):
        if n % 5 == 0 and n % 3 == 0:
            print("FizzBuzz", end=" ")
        elif n % 3 == 0:
            print("Fizz", end=" ")
        elif n % 5 == 0:
            print("Buzz", end=" " if n != 100 else "")
        else:
            print(n, end=" ")
