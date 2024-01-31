#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new_list = []

    for k, v in a_dictionary.items():
        new_list.append(k)
    new_list = sorted(new_list)

    for i in new_list:
        print("{}: {}".format(i, a_dictionary[i]))
