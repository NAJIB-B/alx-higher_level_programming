#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv
    result = 0

    if len(argv) > 1:
        for i in range(len(argv)):
            if i == 0:
                continue
            else:
                result += int(argv[i])
    print(result)
