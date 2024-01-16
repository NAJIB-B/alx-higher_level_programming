#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    print(f"{number%10:d}", end="")
    return (number % 10)
