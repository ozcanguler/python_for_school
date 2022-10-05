def right():
    turn_left()
    turn_left()
    turn_left()
turning=1    
while turning>0:
    if not at_goal():
        if not wall_on_right() and front_is_clear():
            right()
        if front_is_clear():
            move()
        if wall_in_front() and wall_on_right():
            turn_left()
    else:
        turning=0
        
        

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
