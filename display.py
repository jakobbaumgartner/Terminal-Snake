
import random 
import os

class Display:

    size = 32 # size of board (size x size)
    border_coordinates = [] # list of border coordinates, to detect crossings
    food = [5,5,1] # food on the border, 1 - exists, 0 - eaten
    color = 2
    score = 0 # score of the game

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
       # detects if border has been crossed, if it has, it returns True, else False
        crossing_status = False

        for element in self.border_coordinates:
            if(body[0][0] == element[0] and body[0][1] == element[1]):
                crossing_status =  True
            
        return crossing_status


    def SpawnFood(self, body):
        # any time it is called it spawns food somewhere on the board, but not on top of the snake
        # and displays it

        os.system('color 0{}'.format(self.GenerateColor()))

        generateagain = 1 

        while(generateagain == 1): # if food is not on the right place we try generating it again
            generateagain = 0 
            self.food = [random.randint(5,self.size+2), random.randint(6,2+self.size*2), 1] # display food, not close to border

            for element in body: # if on top of snake, try again
                if (self.food[0] == element[0] and self.food[1] == element[1]):
                    generateagain = 1
            if (self.food[0] == element[0]+1 and self.food[1] == element[1]):  # if too close to head try again
                 generateagain = 1
            if (self.food[0] == element[0]-1 and self.food[1] == element[1]):  # if too close to head try again
                generateagain = 1
            if (self.food[0] == element[0] and self.food[1] == element[1]+1):  # if too close to head try again
                generateagain = 1
            if (self.food[0] == element[0] and self.food[1] == element[1]-1):  # if too close to head try again
                generateagain = 1


        print("\033[{};{}HX".format(self.food[0],self.food[1]),end="") # display food


    def EatFood(self, body):
        # if we eat food, we generate new one and return True

              
        if(body[0][0] == self.food[0] and body[0][1] == self.food[1]):
            self.SpawnFood(body)
      
            self.score += 1        # increase score by one point

            return True

        else:
             return False

    def GenerateColor(self):
        #just changes color to random other color

        newcolor = random.randint(0,15)

        if(newcolor == 10):
            newcolor = 'A'
        
        if(newcolor == 11):
            newcolor = 'B'

        if(newcolor == 12):
            newcolor = 'C'

        if(newcolor == 13):
            newcolor = 'D'    
        
        if(newcolor == 14):
            newcolor = 'E'

        if(newcolor == 15):
            newcolor = 'F'

        while(newcolor == self.color or newcolor == 8):
            
            newcolor = random.randint(0,15)

            if(newcolor == 10):
                newcolor = 'A'
            
            if(newcolor == 11):
                newcolor = 'B'

            if(newcolor == 12):
                newcolor = 'C'

            if(newcolor == 13):
                newcolor = 'D'    
            
            if(newcolor == 14):
                newcolor = 'E'

            if(newcolor == 15):
                newcolor = 'F'
        
        self.color = newcolor
        
        return newcolor
        

    def DisplayScore(self):
         print("\033[5;{}HPOINTS:".format(self.size*2 + 8),end="") # display score
         print("\033[7;{}H{}".format(self.size*2 + 8, self.score),end="") # display score
         print("\033[{};0H".format(self.size+5))
     
    def NewGame(self):
        
        food = [5,5,1] # food on the border, 1 - exists, 0 - eaten
        color = 2
        score = 0 # score of the game

