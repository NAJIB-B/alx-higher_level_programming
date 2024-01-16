#!/usr/bin/python3
for i in range(0, 9):
    for j in range(1, 10):
        if i == 0 and j == 1:
            print(f"{i:d}{j:d}", end="")
        print(f", {i:d}{j:d}", end="")
print("")
