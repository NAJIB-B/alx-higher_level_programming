#!/usr/bin/python3
def uppercase(str):
    for i in str:
        value = ord(i)
        if  value > 96 and value < 123: 
            value -= 32
        print(f"{value:c}", end="")
    print("")
uppercase("Best School 98 Battery street")
