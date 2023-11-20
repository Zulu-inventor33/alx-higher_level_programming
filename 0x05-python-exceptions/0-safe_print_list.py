#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    take = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            take += 1
        except IndexError:
            break
    print()
    return(take)
