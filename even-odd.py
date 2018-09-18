print("Welcome to Kev's Even/Odd evaluator, press 0 to exit")
cont = True

while cont == True:
    number = int(input("Enter an Integer: "))
    if number == 0:
        print("Exiting")
        cont = False  
    elif number % 2 == 0:
        print("Integer is Even")     
    else:
        print("Integer is Odd")