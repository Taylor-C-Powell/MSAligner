# Taylor C. Powell
# q9.py
# 2025-9-2

# --------------------------------- FUNCTIONS -----------------------------------------------

# FUNCTION: print_grid
# This function prints a grid of specified dimensions using ASCII characters.
def print_grid(lines=3, columns=3):
    # IF input values are not integers, throw error
    if not isinstance(lines, int) or not isinstance(columns, int):
        print("ERROR: Input values must be integers")
        return
    # IF either input value is less than 2, throw error
    elif lines < 2 or columns < 2:
        print("ERROR: There must be at least 2 lines and 2 columns")
        return
    # IF either input value is greater than 20, throw error
    elif lines > 20 or columns > 20:
        print("ERROR: Too many lines or columns (please have some restraint)")
        return
    # IF both input values are valid, print the grid
    else:
        for i in range(lines-1):
            print("+----" * (columns-1) + "+")
            for j in range(4):
                print("|    " * (columns-1) + "|")
        print("+----" * (columns-1) + "+")
        return


# ------- TESTING -------

print_grid()
print()

print_grid(4, 4)
print()

print_grid(2, 2)
print()

print_grid(2.0, 2.0)
print()

print_grid(2.5, 2.5)
print()

print_grid(2, 1)
print()

print_grid(2, 0)
print()

print_grid(1, 1)
print()

print_grid(0, 0)
print()

print_grid(-1, -1)
print()

print_grid(10)
print()

print_grid(10, 10)
print()

print_grid(20, 20)
print()

print_grid(21, 21) 
print()

print_grid(100, 100)
print()


