def calculator():
    number1 = input("Enter First Number:")
    number2 = input("Enter Second Number:")

    print("What calculation do you want to do")
    Operation = "Addition\nSubtraction\nMultiplication\nDivision\nDivision[remainder]"
    print(Operation)

    operationType = input("Enter operation:")

    if operationType == "Addition":
        print("Result = " + str(int(number1) + int(number2)))
    elif operationType == "Subtraction":
        print("Result = " + str(int(number1) - int(number2)))
    elif operationType == "Multiplication":
        print("Result = " + str(int(number1) * int(number2)))
    elif operationType == "Division":
        print("Result = " + str(int(number1) / int(number2)))
    else:
        print("Result = " + str(int(number1) % int(number2)))

    loop = input("Do you want to restart? Yes or No: ")

    if loop == "yes":
        calculator()
    else:
        print("Turned off")

calculator()




