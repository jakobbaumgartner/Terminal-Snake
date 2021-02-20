# 2D terminal canvas render
class Display:

    size = 32 # size of board (size x size)
 
    def erase (self):
        # go to the top of the terminal and erase the entire screen

        print("\033[H \033[J")  
        return 0


    def displayboard (self):
        # display empty board on the screen

         height = self.size
         width = self.size
 

        # display board with border:
         print("")
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

