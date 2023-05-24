boarder = "\n\033[0;39m==================================================="
# make a class calcu
class Calculator:
    def Add(n1, n2):
        result = n1 + n2
        return result
    
    def Subtract(n1, n2):
        result = n1 - n2
        return result
    
    def Multiply(n1, n2):
        result = n1 * n2
        return result
    
    def Divide(n1, n2):
        try:
            result = n1 / n2
            return result
        except ZeroDivisionError:
            print("\n\033[0;31m[The input cannot be divided to zero !]")

# make a class display
class Display:
    def display_menu():
        print ("\n\033[0;39m===================================================")
        print ("                      MENU                         ")
        print ("===================================================")
        print ("\n     1.Add (+)")
        print ("     2.Subtract (-)")
        print ("     3.Multiply (x)")
        print ("     4.Divide (÷)")
        print ("\n===================================================")
    
    def get_choice():
        # Ask user to choose one of the 4 math operations(+)(-)(x)(÷)
    # use exception if the input is not number; display error message and try again
        while True:
            try:
                choice = int(input("\n\033[0;33mWhat Math Operation will you choose? (1-4): \033[0;39m"))
                if choice < 5 and choice >= 1:
                    break
            except ValueError:
                print("\n\033[0;31m[The input is not a number!]")
            else:  
                print("\n\033[0;31m[The input is not from 1-4]")

    def get_number():
        # Ask user to input 2 numbers
        # use exception if the input is not number; display error message and try again
        while True:
            try:
                n1, n2 = map(float,input("\n\033[0;33mEnter two numbers (put space in between): \033[0;39m").split())
                return n1, n2
            except ValueError:
                print("\n\033[0;31m[The input is not a number or not enough values inputted!]")
    
    def try_again():
        # Ask if the user wants to try again or not (yes or no) 
        # use exception if the input is not yes or no; display error message and try again
        # if yes repeat program; if no display "Thank you!" 
        tryagain= input("\n\033[0;32mDo you want to try again? (yes or no): \033[0;39m")
        while tryagain.lower() != "yes" and tryagain.lower() != "no":
            print ("\n\033[0;31m[The input is not (yes or no)]")
            tryagain= input("\n\033[0;32mDo you want to try again? (yes or no): \033[0;39m")
