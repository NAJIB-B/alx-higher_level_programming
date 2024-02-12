#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    result = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)
        except ZeroDivisionError:
            result = 0
            print("division by 0")
            new_list.append(result)
            pass
        except TypeError:
            result = 0
            print("wrong type")
            new_list.append(result)
            pass
        except IndexError:
            result = 0
            print("out of range")
            new_list.append(result)
            pass
        finally:
            pass
    return (new_list)
