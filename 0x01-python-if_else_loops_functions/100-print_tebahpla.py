#!/usr/bin/python3
letter, switch = 91, 1

for i in range(26):
    if switch == 1:
        letter += 31
        switch = 0
    else:
        letter -= 33
        switch = 1
    print("{:c}".format(letter), end="")
