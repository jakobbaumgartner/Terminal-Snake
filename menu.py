class Menu:

    mode = 0

    def DisplayMenu(self, size):
        # print("                -------- A PYTHON SNAKE GAME -------- ")
        print("\033[{};{}H                -------- A PYTHON SNAKE GAME -------- ".format(2,0),end="") 
        print("\033[{};{}H                       (by Jakob Baumgartner) ".format(3,0),end="") 
        print("\033[{};{}H1. Play Game".format(6,size-8),end="") 
        print("\033[{};{}H2.  Points".format(8,size-6),end="") 
        print("\033[{};{}H3. Options".format(10,size-4),end="") 
        print("\033[{};{}HPlease enter number 1-3.".format(14,size-8),end="") 
        
        print("\033[{};0H".format(15)) # move to the bottom of the screen
     