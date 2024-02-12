# This the sections that we are going to make the calculations
# we are using mathematical_things to make thus calculations.
def mathematical_things():
    try:
        num1 = float(input("\nPlease insert first number:")) # we are asking for a float input for the first number.
        operator = input("Please input one of the following operators(+,-,*,/):") # The user can choose from four operators.
        num2 = float(input("Please insert second number:")) # we are asking for a float input here as well for division purposes.
    
# we using a if-elif-else statement so that the user can choose between different operators when inserted.
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

# we are using f-string to make the equation in a correct and meaningful way.
        equation = f"{num1} {operator} {num2} = {result}" 
        print("\nResult:",equation)

# we are opening the file equation.txt to save all inputs and results being made 
        with open("equations.txt", "a") as file : # using this function, we will save all calculations in the form of equation above.
            file.write(equation + "\n")   # file.write is used to write the calculations of the user into the file.

# these are exceptions that will catch if the user does not input a correct numner and if the user divides into zero    
    except ValueError:
        print("\ninvalid numbers... Please insert numbers only.")
    except ZeroDivisionError:
        print("\nNumbers cannot be divided by zero...Please try again.")

# this function will call all previous made calculations in the file equation.txt.
# file.readlines() will read through all the previously made calculations with the corresponding lines.
# we are using a for loop to reiterate through the calculations made.
def p_made_calculations():
    try:
        with open("equations.txt", "r") as file: 
            previous_calculations = file.readlines()
            for equation in previous_calculations:              
                print(equation.strip())
            else:
                print("\nNo more previous calculations")
                return

# This will catch the error if there is no file found.       
    except FileNotFoundError:
        print("\nEquation file not found.")


# this is the menu that the user can choose from when using the app.
# There are three options and if the user chooses not to do any calculations or look at any then the user can exist the app.
while True:
    try:
        print("\nPlease choose from the following options")
        option = int(input("\nChoose 1 to make a calculation, 2 to display previous calculations or 3 to exit: "))
        
        if option == 1:
            mathematical_things()
        elif option == 2:
            p_made_calculations()
        elif option == 3:
            print("\nThank you.")
            break
        else:
            print("\nPlease insert either 1, 2 or 3 as an option.")
    
    except ValueError:
        print("\nPlease insert either 1, 2 or 3 as an option.")