#!/usr/bin/python3

def safe_print_division(x, y):
    """Returns the division of a by b."""
    try:
        div = x / y
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
