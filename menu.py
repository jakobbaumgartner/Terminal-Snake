class Menu:

    mode = 0

    def DisplayMenu(self, size):
        # print("                -------- A PYTHON SNAKE GAME -------- ")
        print("\033[{};{}H                -------- A PYTHON SNAKE GAME -------- ".format(2,0),end="") 
        print("\033[{};{}H                       (by Jakob Baumgartner) ".format(3,0),end="") 
        print("\033[{};{}H1. Play Game {} x {}".format(6,25,size, size),end="") 
        print("\033[{};{}H    Size of board".format(8,25),end="") 
        print("\033[{};{}H    2. 8 x 8".format(10,27),end="") 
        print("\033[{};{}H    3. 16 x 16".format(12,27),end="") 
        print("\033[{};{}H    4. 32 x 32".format(14,27),end="") 
        print("\033[{};{}HPlease enter number 1-4.".format(17,24),end="") 
        
        print("\033[{};0H".format(15)) # move to the bottom of the screen
     