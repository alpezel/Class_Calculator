boarder = "\n\033[0;39m==================================================="
# Make a class calculator
class Calculator:
    @staticmethod
    def Add(n1, n2):
        return n1 + n2

    @staticmethod
    def Subtract(n1, n2):
        return n1 - n2

    @staticmethod
    def Multiply(n1, n2):
        return n1 * n2

    @staticmethod
    def Divide(n1, n2):
        try:
            result = n1 / n2
            return result
        except ZeroDivisionError:
            print("\n\033[0;31m[Error: Division by zero is not allowed!]")
        
# Make a class display
class Display:
    @staticmethod
    def show_menu():
        print(boarder,"\n")
        print("                      MENU                         ")
        print(boarder)
        print("\n     1.Add (+)")
        print("     2.Subtract (-)")
        print("     3.Multiply (x)")
        print("     4.Divide (÷)")
        print("\n" + boarder)

    @staticmethod
    def get_choice():
        # Ask user to choose one of the 4 math operations(+)(-)(x)(÷)
        # use exception if the input is not number; display error message and try again
        while True:
            try:
                choice = int(input("\n\033[0;33mWhat Math Operation will you choose? (1-4): \033[0;39m"))
                if 1 <= choice <= 4:
                    return choice
            except ValueError:
                print("\n\033[0;31m[The input is not a number!]")
            else:
                print("\n\033[0;31m[The input is not from 1-4]")

    @staticmethod
    def get_numbers():
        # Ask user to input 2 numbers
        # use exception if the input is not number; display error message and try again
        while True:
            try:
                n1, n2 = map(float, input("\n\033[0;33mEnter two numbers (put space in between): \033[0;39m").split())
                return n1, n2
            except ValueError:
                print("\n\033[0;31m[The input is not a number or not enough values inputted!]")

    @staticmethod
    def try_again():
        # Ask if the user wants to try again or not (yes or no) 
        while True:
            tryagain = input("\n\033[0;32mDo you want to try again? (yes or no): \033[0;39m")
            if tryagain.lower() == "yes" or tryagain.lower() == "no":
                return tryagain.lower()
            # display error message if input is not yes or no, and try again
            print("\n\033[0;31m[The input is not (yes or no)]")