class Snake:


    # location = [25,25] # current location of the head of the snake

    direction = 3 # direction of moving of the snake
    # 0 - up
    # 1 - down
    # 2 - left
    # 3 - right

    body = [[25,25,0],[26,25,1],[27,25,1],[28,25,1]]
    #[y,x,element_type]
    # element type:
    # 0 - head
    # 1 - body

    removed = [] # saves removed element

   
    def SnakeMove (self):
       # snake moves in the direction that was chosen

    # snake move function:
    # - remove the last element 
    # - change the type of the first element to BODY 
    # - add an element type HEAD to the beginning ( in the chosen DIRECTION) 


       self.removed = self.body.pop() #remove the last element

       (self.body[0])[2] = 1

       if self.direction == 0: 
           ycoord = ((self.body[0])[0] - 1) # when moving up, we decrease y - coord by one
           xcoord = (self.body[0])[1] # x - coord is the same as elements before it

       if self.direction == 1: 
           ycoord = ((self.body[0])[0] + 1) # when moving down, we increase y - coord by one
           xcoord = (self.body[0])[1] # x - coord is the same as elements before it

       if self.direction == 2:
           ycoord = (self.body[0])[0] # moving left, y - coord is the same as the element before
           xcoord = ((self.body[0])[1] - 1) # x - coord is for one shifted to the left

       if self.direction == 3:
           ycoord = (self.body[0])[0] # moving right, y - coord is the same as the element before
           xcoord = ((self.body[0])[1] + 1) # x - coord is for one shifted to the right

       self.body.insert(0,[ycoord,xcoord,0]) # add an element (HEAD) to the beginning

    def ChangeDirection(self, pressed_key):
        # reads the input and converts it to change in direction

        if (pressed_key == 'w' and self.direction != 1):
            self.direction = 0

        if (pressed_key == 's' and self.direction != 0):
            self.direction = 1

        if (pressed_key == 'a' and self.direction != 3):
            self.direction = 2
        
        if (pressed_key == 'd' and self.direction != 2):
            self.direction = 3

            