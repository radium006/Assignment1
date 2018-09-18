from calculator import add, subtract, multiply, divide

print("Welcome to Kev's simple calculator")
cont = True
while cont == True:


    number_1 = int(input("Enter num1: "))
    operand = input('Enter operand: ')
    number_2 = int(input('Enter num2: '))

    if operand == "+":
        result = add(number_1, number_2)
    elif operand == '-':
        result = subtract(number_1,number_2)
    elif operand == '*':
        result = multiply(number_1,number_2)
    elif operand == '/':
        result = divide(number_1,number_2)
    else:
        print("ERROR: INVALID OPERAND")    
    
    print("Your equation is {0} {1} {2} = {3}".format(number_1,operand,number_2,result))
    
    option = input("Would you like to continue? y/n: ")
    
    if option == "n":
        print("EXITING")
        cont = False
    elif option != 'y':
        print("Invalid Input, EXITING")
    