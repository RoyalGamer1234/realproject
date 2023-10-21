def PrintInversetriangle(number):
    for row in range(number, 0, -1):
        # Print leading spaces
        for space in range(number - row):
            print(" ", end='')
        # Print 'x' characters
        for x_char in range(row):
            print("x", end='')
        # Move to the next line after each row
        print()

# Call the function with the desired number of rows





number = input("enter")
number = int(number)
PrintInversetriangle(number)
