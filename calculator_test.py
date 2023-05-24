from calculator_with_class import Calculator 
from calculator_with_class import Display

calc = Calculator()
menu = Display()

while True:
    





        

        
    # Use if statements to check the choices and call the corresponding function 
    # Display result    
    if choice == 1:
        sum = Add()
        print("\n\033[0;36mResult:",sum)
        print(boarder)
    elif choice==2:
        diff=Subtract()
        print ("\n\033[0;36mResult:",diff)
        print(boarder)
    elif choice==3:
        prod=Multiply()
        print ("\n\033[0;36mResult:",prod)
        print(boarder)
    elif choice ==4:
        quot=Divide()
        print ("\n\033[0;36mResult:",quot)
        print(boarder)

    

    if tryagain.lower() == "no":
        print(boarder,"\n")
        print ("\033[0;34mThank you!")
        print(boarder,"\n")
    break