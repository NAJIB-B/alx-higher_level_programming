#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_digit = number % 10
    print(f"Last digit of {number:d} is {number%10}", end=" ")
else:
    copy = -number
    last_digit = -(copy % 10)
    print(f"Last digit of {number:d} is {last_digit}", end=" ")
if last_digit < 6 and last_digit != 0:
    print("and is less than 6 and not 0")
elif last_digit > 5:
    print("and is greater than 5")
else:
    print("and is 0")
