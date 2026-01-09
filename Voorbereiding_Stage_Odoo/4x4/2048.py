# 4*4 grid
# initially 2 random squares are filled with number 2, the rest are empty
# We have to press any one of four keys to move up, down, left, or right. 
# When we press any key, the elements of the cell move in that direction such that if any two identical numbers are contained in that particular row 
# (in case of moving left or right) or column 
# (in case of moving up and down) they get add up and extreme cell in that direction fill itself with that number and rest cells goes empty again.
# After this grid compression, a random square is filled with number 2


import logic

if __name__== "__main__":
    
    mat = logic.start_game()
    
while True:
    
    x = input("Enter the command: ")
    if (x == 'w' or x == "W"):
        mat , flag = logic.moveUp(mat)
        
        status = logic.getCurrentGameState(mat)
        print(status)
        
        if (status == 'GAME NOT OVER'):
            logic.addNew2(mat)
        else:
            break
        
    elif (x == 's' or x == "S"):
        mat , flag = logic.moveDown(mat)
        
        status = logic.getCurrentGameState(mat)
        print(status)
        
        if (status == 'GAME NOT OVER'):
            logic.addNew2(mat)
        else:
            break
        
    elif (x == 'a' or x == "A"):
        mat , flag = logic.moveLeft(mat)
        
        status = logic.getCurrentGameState(mat)
        print(status)
        
        if (status == 'GAME NOT OVER'):
            logic.addNew2(mat)
        else:
            break   
    
    elif (x == 'd' or x == "D"):
        mat , flag = logic.moveRight(mat)
        
        status = logic.getCurrentGameState(mat)
        print(status)
        
        if (status == 'GAME NOT OVER'):
            logic.addNew2(mat)
        else:
            break
        
    else:
        print("Invalid Input")
        
    print(mat)
