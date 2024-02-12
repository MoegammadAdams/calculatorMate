# We are defining a function so that we can call it later when the user calls it.
def mathematical_calculations():
    try:
        num1 = float(input("\nPlease insert first number:"))
        operator = input("Please input one of the following operators(+,-,*,/):")
        num2 = float(input("Please insert second number:"))
    
    # We are using if-elif-else function so that we can get the correct operator which the user requests.
    # Also if the user doesnt input a integer then the valueerror exceptions will detect the error and request an integer.
    # If there isnt a correct operator inputted then the else function will kick in and inform user to input the correct operator.
    # '+' is for addition
    # '-' is for subtraction
    # '*' is for multiplication
    # '/' is used for division
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1*num2
        elif operator == "/":
            result = num1/num2
        else:
            print("\nYou have inserted incorrect operator...Please try again.")
            return

        equation = f"{num1} {operator} {num2} = {result}" 
        print("\nResult:",equation)

        with open("equations.txt", "a") as file : # using this function, we will save all calculations in the form of equation above.
            file.write(equation + "\n")   # file.write is used to write the calculations of the user into the file.
    
    except ValueError:
        print("\ninvalid numbers... Please insert numbers only.")
    except ZeroDivisionError:
        print("\nNumbers cannot be divided by zero...Please try again.")
# These exceptions are used to put the program when it has ran into a error.
# This will inform us what type of error it is and how we can avoid it.
# valueError will display that an integer needs to be inputted.
# ZeroDivsionError will display that divsion will not work when there is a zero/0

# this function will open and read the file but will not write in it.
# "r" is used to read and we use the for function to read each of the calculations made previously.
def previously_made_calculations():
    try:
        with open("equations.txt", "r") as file: 
            previous_calculations = file.readlines()
            for equation in previous_calculations:              
                print(equation.strip())
            else:
                print("\nNo more previous calculations")
                return
        
    except FileNotFoundError:
        print("\nEquation file not found.")
# This exception will ensure that the user knows that the file does not exist.
# It will also stop the program from continuing because there is no file to read.

# We are using if-elif-else function to give the user a choice whether to make a calculation or display the previous ones.
# Once the user chose the correct option then we use if-elif-else to call that specific function.
# once the function is called then we will either make a calculation or display all previous ones.
# We are using the except ValueError to ensure that the user knows that he has only three options to choose from.
# the try exception block assist will loop everytime an incorrect option is chosen.
while True:
    try:
        print("\nPlease choose from the following options")
        option = int(input("\nChoose 1 to make a calculation, 2 to display previous calculations or 3 to exit: "))
        
        if option == 1:
            mathematical_calculations()
        elif option == 2:
            previously_made_calculations()
        elif option == 3:
            print("\nThank you.")
            break
        else:
            print("\nPlease insert either 1, 2 or 3 as an option.")
    
    except ValueError:
        print("\nPlease insert either 1, 2 or 3 as an option.")