from calculator_with_class import Calculator 
from calculator_with_class import Display
boarder = "\n\033[0;39m==================================================="
# Create instances of the classes
calc = Calculator()
menu = Display()

while True:
    menu.show_menu()
    choice = menu.get_choice()
    n1, n2 = menu.get_numbers()
    
    # Use if statements to check the choices and call the corresponding function 
    # Display result
    if choice == 1:
        result = calc.Add(n1, n2)
    elif choice == 2:
        result = calc.Subtract(n1, n2)
    elif choice == 3:
        result = calc.Multiply(n1, n2)
    elif choice == 4:
        result = calc.Divide(n1, n2)

    print("\n\033[0;36mResult:", result)
    print(boarder)

     # if yes repeat program; if no display "Thank you!" 
    try_again = menu.try_again()
    if try_again == "no":
        print(boarder,"\n")
        print("\033[0;34mThank you!")
        print(boarder)
        break