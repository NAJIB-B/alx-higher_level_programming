#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if not my_list or x == 0:
        return (0)
    j = 0
    try:
        while j <= x:
            print(my_list[j], end="")
            j += 1
    except IndexError:
        print("")
        return (i)

    print("")
    return (i)
