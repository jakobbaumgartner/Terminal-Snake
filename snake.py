class Snake:


    # location = [25,25] # current location of the head of the snake

    direction = 2 # direction of moving of the snake
    # 0 - up
    # 1 - down
    # 2 - left
    # 3 - right

    body = [[25,25,0],[25,26,1],[25,27,1],[25,28,1]]
    #[y,x,element_type]
    # element type:
    # 0 - head
    # 1 - body

   
    def SnakeMove (self):
       # snake moves in the direction that was chosen

       self.body.pop() #remove the last element

       (self.body[0])[2] = 1

       if self.direction == 2:
           ycoord = (self.body[0])[0] # moving left, y - coord is the same as the element before
           xcoord = ((self.body[0])[1] - 1) # x - coord is for one shifted to the left

       if self.direction == 3:
           ycoord = (self.body[0])[0] # moving right, y - coord is the same as the element before
           xcoord = ((self.body[0])[1] + 1) # x - coord is for one shifted to the right

       self.body.insert(0,[ycoord,xcoord,0]) # add an element (HEAD) to the beginning