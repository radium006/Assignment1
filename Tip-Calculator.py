print("Welcome to Kev's Tip Calculator")
cont = True

while cont == True:
    
    total = float(input("Enter your bill's total: "))
    tipTotal = float(input("Enter desired tip as a whole percent number: ")) / 100
    
    total = total + (total * tipTotal)
    
    print("Your bill total is {0}".format(total, '05'))
    
    option = input("Would you like to continue? y/n: ")
    
    if option == "n":
        print("EXITING")
        cont = False
        
    elif option != 'y':
        print("Invalid Input, EXITING")
        cont = False
    