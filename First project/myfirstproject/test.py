def calculator():
    number1 = input("Enter First Number:")
    number2 = input("Enter Second Number:")

    print("What calculation do you want to do")
    operation = "Addition\nSubtraction\nMultiplication\nDivision\nDivision[remainder]"
    print(operation)

    operationType = input("Enter operation:")
    print("operationType")
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

calculator()
loop = input("Do you want to restart? Yes or No: ")
print("loop = " + loop)
while loop == "Yes":
    calculator()
    loop = input("Do you want to restart? Yes or No: ")
if loop == "No":
    print("Turned off")
