#!/usr/bin/python3

def safe_print_list(my_list=[], y=0):
    """Print y elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        y (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(y):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
