from calculator_with_class import Calculator

class Numbers(Calculator):

    def Sign (self, n1,n2):
        if n1 > 0:
            print("\033[0;36mThe first number:","\033[0;39m",n1,"\033[0;36mis \033[0;46mPOSITIVE\033[0;36m")
        elif n1 < 0:
            print("\033[0;36mThe first number:","\033[0;39m",n1,"\033[0;36mis \033[0;41mNEGATIVE\033[0;39m")
        elif n1 == 0:
            print("\033[0;36mThe first number:","\033[0;39m",n1,"\033[0;36mis neither \033[0;46mPOSITIVE \033[0;36mnor \033[0;41mNEGATIVE\033[0;39m")
        
        if n2 > 0:
            print("\033[0;36mThe second number:","\033[0;39m",n2,"\033[0;36mis \033[0;46mPOSITIVE\033[0;36m")
        elif n2 < 0:
            print("\033[0;36mThe second number:","\033[0;39m",n2,"\033[0;36mis \033[0;41mNEGATIVE\033[0;39m")
        elif n2 == 0:
            print("\033[0;36mThe second number:","\033[0;39m",n2,"\033[0;36mis neither \033[0;46mPOSITIVE \033[0;36mnor \033[0;41mNEGATIVE\033[0;39m")
        

        
        