#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list:
        new_list = []
        for i in my_list:
            if (i % 2) == 0:
                new_list.append(true)
            else:
                new_list.append(false)
        return new_list
