def FizzBuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print("NO FIZZYBUZZY")

cont = True

while cont == True:
    num = int(input("Enter an integer or press 0 to exit: "))
    if num != 0:
        FizzBuzz(num)
    else:
        print("EXITING")
        cont = False
