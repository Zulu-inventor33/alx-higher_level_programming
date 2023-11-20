#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divd = a / b
    except (ZeroDivisionError, FloatingPointError):
        divd = None
    finally:
        print("Inside result: {}".format(divd))
    return divd
