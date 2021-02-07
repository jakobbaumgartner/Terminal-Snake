class Snake:

    location = [25,25] # current location of the head of the snake
    direction = 0 # direction of moving of the snake
    # 0 - up
    # 1 - down
    # 2 - left
    # 3 - right

    body = [[25,25],[25,26],[25,27],[25,28]]

    # if we gain a part we add it to the end of the snake
    # we allways only update the line the last part is on before moving and the line head is on 
            # that is first and last line of the snake (last before update, first after)