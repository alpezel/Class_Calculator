from calculator_with_class import Calculator
from calculator_with_class import Display

class Extra(Display):
    def boarder(self):
       boarder_line = "\n\033[0;39m==================================================="
       return boarder_line