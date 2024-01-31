#!/usr/bin/python3

def uniq_add(my_list=[]):
    the_set = set(my_list)
    uniq_list = list(the_set)

    total = 0

    for i in uniq_list:
        total += i
    return total
