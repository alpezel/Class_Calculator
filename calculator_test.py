from calculator_with_class import Calculator 
from calculator_with_class import Display
boarder = "\n\033[0;39m==================================================="
calc = Calculator()
menu = Display()

while True:
    menu.display_menu()
    choice = menu.get_choice()
    n1, n2 = menu.get_number()

    # Use if statements to check the choices and call the corresponding function 
    # Display result    
    if choice == 1:
        sum = calc.Add(n1,n2)
        print("\n\033[0;36mResult:",sum)
        print(boarder)
    elif choice==2:
        diff = calc.Subtract(n1,n2)
        print ("\n\033[0;36mResult:",diff)
        print(boarder)
    elif choice==3:
        prod = calc.Multiply(n1,n2)
        print ("\n\033[0;36mResult:",prod)
        print(boarder)
    elif choice ==4:
        quot = calc.Divide(n1,n2)
        print ("\n\033[0;36mResult:",quot)
        print(boarder)

    
    try_again = menu.try_again()
    if  try_again == "no":
        print(boarder,"\n")
        print ("\033[0;34mThank you!")
        print(boarder,"\n")
    break