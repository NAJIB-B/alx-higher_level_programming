#!/usr/bin/python3


if __name__ == "__main__":
     """Print the number of and list of arguments."""
    import sys

    argv = sys.argv

    if (len(argv) == 1):
        print("0 arguments.")
    if (len(argv) == 2):
        print("1 argument:\n1: Hello")
    if (len(argv) > 2):
        print("{} arguments:".format(len(argv) - 1))
        for i in range(len(argv)):
            if i == 0:
                continue
            else:
                print("{}: {}".format(i, argv[i]))  
