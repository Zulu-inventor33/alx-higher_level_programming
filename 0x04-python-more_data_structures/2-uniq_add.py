#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    rex = 0
    for i in new:
        rex += i
    return rex
