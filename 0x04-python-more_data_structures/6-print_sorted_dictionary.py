#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new_list = []

    for k, v in a_dictionary:
        new_list.append(k)
    return sorted(new_list)
