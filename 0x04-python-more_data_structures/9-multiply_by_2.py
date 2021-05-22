#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = dict(a_dictionary)
    for i in new_dictionary:
        # keys are inmutables, so it only multiply the value
        new_dictionary[i] *= 2
    return new_dictionary
