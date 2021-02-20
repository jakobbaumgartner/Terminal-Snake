# 2D terminal canvas render
class Display:

    size = 32 # size of board (size x size)
    border_coordinates = [] # list of border coordinates, to detect crossings

    def __init__(self):
        # runs on new object initialization
        
        # add top border
        for element in range(self.size*2+4):
            self.border_coordinates.append([3,element+1])

        # add bottom border
        for element in range(self.size*2+4):
            self.border_coordinates.append([4+self.size,element+1])

        # add left border
        for element in range(self.size):
            self.border_coordinates.append([element+4,3])

        # add right border
        for element in range(self.size):
            self.border_coordinates.append([element+4,4+2*self.size])

        





 
    def Erase (self):
        # go to the top of the terminal and erase the entire screen

        print("\033[H \033[J")  
        return 0


    def DisplayBoard (self):
        # display empty board on the screen

         height = self.size
         width = self.size
 

        # display board with border:
         print("                -------- A PYTHON SNAKE GAME -------- ")
         print("  ", end="")

        # display top border
         for elementx in range(width+1):
             print("##",end="")
         print("")
        

         for elementy in range(height):
             print("  #", end="") # display left border
            
             # display empty board space
             for elementx in range(width):
            
                print("  ", end="")
               
                if elementx == width-1:
                    print("#",end="") # display right border
             print("")
         print("  ",end="")
        

         # display bottom border
         for elementx in range(width+1):
            print("##",end="")


    def DisplaySnake (self, body, removed):
    # draws snake on board

        # first lets draw all the elements
        for element in body:
            if(element[2] == 0):
                print("\033[{};{}HO".format(element[0],element[1]),end="")
            else:
                print("\033[{};{}H#".format(element[0],element[1]),end="")

        # remove the last element
        if(removed != []):
            print("\033[{};{}H ".format(removed[0],removed[1]),end="")
        
        print("\033[{};0H".format(self.size+5))

    def BorderCrossing(self, body):
        # print(body)
        # print(self.border_coordinates)
        for element in self.border_coordinates:
            if(body[0][0] == element[0] and body[0][1] == element[1]):
                print("COROSSEEED")
        else:
            print("                  ")
