# make a class calcu
class Calcu:
    def __init__(self, n1,n2) :
        self.n1 = n1
        self.n2 = n2

    def Add(self):
        result = self.n1 + self.n2
        return result
    def Subtract(self):
        result = self.n1 - self.n2
        return result
    def Multiply(self):
        result = self.n1 * self.n2
        return result
    def Divide(self):
        try:
            result = self.n1 / self.n2
            return result
        except ZeroDivisionError:
            print("\n\033[0;31m[The input cannot be divided to zero !]")

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
        
# Ask user to input 2 numbers
# use exception if the input is not number; display error message and try again
    while True:
        try:
            n1, n2 = map(float,input("\n\033[0;33mEnter two numbers (put space in between): \033[0;39m").split())
        except ValueError:
            print("\n\033[0;31m[The input is not a number or not enough values inputted!]")
        else:
            break    
    


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


       