# remove from calculator_with_class import Calculator
from calculator_with_class import Display
# imported Numbers class and change the calculator class
from inheritance_calcu import Numbers

boarder = "\n\033[0;39m==================================================="
# Create instances of the classes
menu = Display()
# remove calc = Calculator(), since its in the Numbers class
nums = Numbers()

while True:
    menu.show_menu()
    choice = menu.get_choice()
    n1, n2 = menu.get_numbers()
    
    # Use if statements to check the choices and call the corresponding function 
    # Display result
    # change calc. to nums. to apply inheritance 
    if choice == 1:
        result = nums.Add(n1, n2)
    elif choice == 2:
        result = nums.Subtract(n1, n2)
    elif choice == 3:
        result = nums.Multiply(n1, n2)
    elif choice == 4:
        result = nums.Divide(n1, n2)

    print("\n\033[0;36mResult:", result,"\n")
    # pront the sign of the inputted number
    sign = nums.Sign(n1,n2)
    print(boarder)

     # if yes repeat program; if no display "Thank you!" 
    try_again = menu.try_again()
    if try_again == "no":
        print(boarder,"\n")
        print("\033[0;34mThank you!")
        print(boarder)
        break