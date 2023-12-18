#!/usr/bin/pythoy3

def safe_print_list(my_list=[], x=0):
    printed_elements = 0

    try:
        for i in range(x):
            print(my_list[i], end=' ')
            printed_elements += 1
    except IndexError:
        pass  # Handles the case where index is out of range

    print()  # Prints a new line after all elements

    return (printed_elements)
