def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0
    try:
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end=" ")
                printed_integers += 1
    except (TypeError, IndexError):
        pass  # Skips exceptions silently

    print("")  # Print a new line after all integers
    return printed_integers
