from calculator_with_class import Calculator
from calculator_with_class import Display

class Numbers(Calculator):

    def Sign (self, n1,n2):
        if n1 > 0:
            print("the first number is POSITIVE ")
        elif n1 < 0:
            print("the first number is NEGATIVE ")
        elif n1 == 0:
            print("the first number is neither POSITIVE nor NEGATIVE ")
        
        if n2 > 0:
            print("the first number is POSITIVE ")
        elif n2 < 0:
            print("the first number is NEGATIVE ")
        elif n2 == 0:
            print("the first number is neither POSITIVE nor NEGATIVE ")
        
        return n1, n2

        
        