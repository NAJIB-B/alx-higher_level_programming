#!/usr/bin/python3
for i in range(0, 9):
    for j in range(1, 10):
        if i == 0 and j == 1:
            print("{:d}{:d}".format(i, j), end="")
        print(", {:d}{:d}".format(i, j), end="")
print("")
