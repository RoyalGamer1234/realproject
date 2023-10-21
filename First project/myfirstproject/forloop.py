def printRightTrianle(number):
    for i in range(1,6):
        print("i=",i)
        for j in range(1,j<=i,1):
            print("j=",j)
            print("*",end='')
        print()

def printSlantingLine(number):
    for rownum in range(1,number+1,1):
        for colnum in range(1,rownum+1,1):
            if rownum == colnum:
                print("*",end='')
            else:
                print(" ",end='')
        print()

def PrintNumberTriangle(number):
    for row in range(1, number + 1):
        for col in range(1, row + 1 ):
            print(col, end="")
        print()

def PrintInversetriangle(number):
    for row in range(1,number,1):
        for col in range(number,0,-1):
            print("*",end='')
        print()









number = input("enter")
number = int(number)
#printRightTrianle(number)
#printSlantingLine(number)
#PrintNumberTriangle(number)
PrintInversetriangle(number)
