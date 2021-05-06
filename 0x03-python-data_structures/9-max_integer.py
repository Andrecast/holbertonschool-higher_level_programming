#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return(None)
    max = my_list[0]  # suponemos q el primero es el max
    # ciclo para ir comparando cada elemento con el primero
    for x in my_list:
        if x > max:
            max = x
    return(max)
