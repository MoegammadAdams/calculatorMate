
def mathematical_things():
    try:
        num1 = float(input("\nPlease insert first number:"))
        operator = input("Please input one of the following operators(+,-,*,/):")
        num2 = float(input("Please insert second number:"))
    
    
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

def p_made_calculations():
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