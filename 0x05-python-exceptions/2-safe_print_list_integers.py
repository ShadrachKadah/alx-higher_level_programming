#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0
    index = 0

    while printed_integers < x:
        try:
            value = my_list[index]
            if isinstance(value, int):
                print("{:d}".format(value), end=" ")
                printed_integers += 1
        except (IndexError, ValueError, TypeError):
            pass
        
        index += 1

    print("")
    return printed_integers

