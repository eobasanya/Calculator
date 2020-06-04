
def add(num1, num2):
    """returns num1 plus num2"""
    return num1 + num2
def subtract(num1, num2):
    """returns num1 minus num2"""
    return num1 - num2
def multiply(num1, num2):
    """returns num1 times num2"""
    return num1 * num2
def divide(num1, num2):
    """returns num1 divided by num2"""
    return num1 / num2

def runOperation(operation, num1, num2):
    if (operation == 1 or operation == '+' or operation == 'add'):
        print("Adding...")
        print(add(num1, num2))

    elif (operation == 2 or operation == '-' or operation == 'subtract'):
        print("Subtracting")
        print(subtract(num1, num2))
    elif (operation == 3 or operation == '*' or operation == 'multiply'):
        print("Multiplying")
        print(multiply(num1, num2))
    elif (operation == 4 or operation == '/' or operation == 'divide'):
        print("Dividing")
        print(divide(num1, num2))
    else:
        print("I don't understand")


def main():

        validinput = False
        while not validinput:
                    # get input
            try:
                num1 = int(input("This is a calculator, what is your first number?"))
                num2 = int(input("Ok, and what is your second number?"))
                operation = int(input("what do you want to do? (1. add, 2. subtract, 3. multiply, 4. divide)"))

            except:
                print("Invalid Entry. Try again")
        # return #ends program here
            runOperation(operation, num1, num2)
            restart = int(input("Would you like to perform another calculation? 1. Yes, 2. No"))
            if restart == 1:
                continue
            elif restart == 2:
                return
                validinput = True


                #print(add(num1,num2)) #
                #print(subtract(num1,num2)) #
                #print(multiply(num1,num2)) #100
                #print(divide(num1,num2)) #5

if __name__ == "__main__":
    main()
