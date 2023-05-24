# make a class calcu
class Calcu:
    def __init__(self) :
        self.n1 = n1
        self.n2 = n2

    def Add():
        result = n1 + n2
        return result
    def Subtract():
        result = n1 - n2
        return result
    def Multiply():
        result = n1 * n2
        return result
    def Divide():
        result = n1 / n2
        return result


# make a class display
class Display:
    boarder = "\n\033[0;39m==================================================="
    def display_menu():
        print ("\n\033[0;39m===================================================")
        print ("                      MENU                         ")
        print ("===================================================")
        print ("\n     1.Add (+)")
        print ("     2.Subtract (-)")
        print ("     3.Multiply (x)")
        print ("     4.Divide (÷)")
        print ("\n===================================================")

    while True:
        try:
            choice = int(input("\n\033[0;33mWhat Math Operation will you choose? (1-4): \033[0;39m"))
            if choice < 5 and choice >= 1:
                break
        except ValueError:
            print("\n\033[0;31m[The input is not a number!]")
        else:  
            print("\n\033[0;31m[The input is not from 1-4]")