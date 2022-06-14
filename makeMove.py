import pygame
import math
import drawGrid as drawG

def gameOver(playingGrid):  #checking if game is over
    for r in range(9):
        for c in range(9):
            if playingGrid[r][c] == 0:
                return False  #still got an empty space
    return True #no more spaces

def getNumber():  #getting user input
    numClickPos = pygame.mouse.get_pos()
    if 505 <= numClickPos[0] <= 566 and 81 <= numClickPos[1] <= 146:
        return 1
    elif  576 <= numClickPos[0] <= 642 and 81 <= numClickPos[1] <= 146:
        return 2
    elif  651 <= numClickPos[0] <= 715 and 81 <= numClickPos[1] <= 146:
        return 3
    elif 505 <= numClickPos[0] <= 566 and 155 <= numClickPos[1] <= 221:
        return 4
    elif  576 <= numClickPos[0] <= 642 and 155 <= numClickPos[1] <= 221:
        return 5
    elif  651 <= numClickPos[0] <= 715 and 155 <= numClickPos[1] <= 221:
        return 6
    elif 505 <= numClickPos[0] <= 566 and 230 <= numClickPos[1] <= 296:
        return 7
    elif  576 <= numClickPos[0] <= 642 and 230 <= numClickPos[1] <= 296:
        return 8
    elif  651 <= numClickPos[0] <= 715 and 230 <= numClickPos[1] <= 296:
        return 9
    else:
        return False

def getCoords(screen, playingGrid, initialGrid, userNum):
    numClickPos = pygame.mouse.get_pos()
    length = 462

    #FIRST SUB-GRID (TOP-LEFT)
    if 0 <= numClickPos[0] <= length/9 and 0 <= numClickPos[1] <= length/9:  
        userRow = 0
        userCol = 0  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 0
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif (length/9)+1 <= numClickPos[0] <= (length/9)*2  and 0 <= numClickPos[1] <= length/9: 
        userRow = 0
        userCol = 1
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 1  #01
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif ((length/9)*2)+1 <= numClickPos[0] <= (length/9)*3 and 0 <= numClickPos[1] <= length/9:
        userRow = 0
        userCol = 2  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 2  #02
        return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    
    elif 6 <= numClickPos[0] <= 50 and 56 <= numClickPos[1] <= 103:
        userRow = 1
        userCol = 0
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 10
        return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)   
    elif 56 <= numClickPos[0] <= 103 and 56 <= numClickPos[1] <= 103:
        userRow = 1
        userCol = 1  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 11
        return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)   
    elif 107 <= numClickPos[0] <= 152 and 56 <= numClickPos[1] <= 103:
        userRow = 1
        userCol = 2  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 12
        return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    
    elif 6 <= numClickPos[0] <= 50 and 107 <= numClickPos[1] <= 149:
        userRow = 2
        userCol = 0
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 20
        return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 56 <= numClickPos[0] <= 103 and 107 <= numClickPos[1] <= 149:
        userRow = 2
        userCol = 1  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 21
        return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)   
    elif 106 <= numClickPos[0] <= 152 and 107 <= numClickPos[1] <= 149:
        userRow = 2
        userCol = 2  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 22
        return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)

    #SECOND SUB-GRID (TOP-MID)
    elif 158 <= numClickPos[0] <= 206 and 7 <= numClickPos[1] <= 51:
        userRow = 0
        userCol = 3
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 3  #03
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 208 <= numClickPos[0] <= 257 and 7 <= numClickPos[1] <= 51:
        userRow = 0
        userCol = 4
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 4  #04
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 259 <= numClickPos[0] <= 305 and 7 <= numClickPos[1] <= 51:
        userRow = 0
        userCol = 5
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 5  #05
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)

    elif 158 <= numClickPos[0] <= 206 and 57 <= numClickPos[1] <= 103:
        userRow = 1
        userCol = 3
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 13  #13
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 208 <= numClickPos[0] <= 257 and 57 <= numClickPos[1] <= 103:
        userRow = 1
        userCol = 4
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 14  #14
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 259 <= numClickPos[0] <= 305 and 57 <= numClickPos[1] <= 103:
        userRow = 1
        userCol = 5
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 15  #15
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)

    elif 158 <= numClickPos[0] <= 206 and 107 <= numClickPos[1] <= 150:
        userRow = 2
        userCol = 3
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 23  #23
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 208 <= numClickPos[0] <= 257 and 107 <= numClickPos[1] <= 150:
        userRow = 2
        userCol = 4
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 24  #24
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 259 <= numClickPos[0] <= 305 and 107 <= numClickPos[1] <= 150:
        userRow = 2
        userCol = 5
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 25  #25
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)

    #THIRD SUB-GRID (TOP-RIGHT)
    elif 310 <= numClickPos[0] <= 358 and 7 <= numClickPos[1] <= 51:  
        userRow = 0
        userCol = 6  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 6 #06
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 360 <= numClickPos[0] <= 408 and 7 <= numClickPos[1] <= 51:
        userRow = 0
        userCol = 7
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 7  #07
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 414 <= numClickPos[0] <= 457 and 7 <= numClickPos[1] <= 51:
        userRow = 0
        userCol = 8
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 8  #08
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    
    elif 310 <= numClickPos[0] <= 358 and 57 <= numClickPos[1] <= 103:  
        userRow = 1
        userCol = 6  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 16
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 360 <= numClickPos[0] <= 408 and 57 <= numClickPos[1] <= 103:
        userRow = 1
        userCol = 7
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 17
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 414 <= numClickPos[0] <= 457 and 57 <= numClickPos[1] <= 103:
        userRow = 1
        userCol = 8
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 18
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)

    elif 310 <= numClickPos[0] <= 358 and 107 <= numClickPos[1] <= 147:  
        userRow = 2
        userCol = 6  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 26
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 360 <= numClickPos[0] <= 408 and 107 <= numClickPos[1] <= 147: 
        userRow = 2
        userCol = 7
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 27
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 414 <= numClickPos[0] <= 457 and 107 <= numClickPos[1] <= 147: 
        userRow = 2
        userCol = 8
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 28
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    
    #FOURTH SUB-GRID (MID-LEFT)
    elif 6 <= numClickPos[0] <= 50 and 157 <= numClickPos[1] <= 203:  
        userRow = 3
        userCol = 0  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 30 #30
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 57 <= numClickPos[0] <= 102 and 157 <= numClickPos[1] <= 203:
        userRow = 3
        userCol = 1
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 31  #31
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 107 <= numClickPos[0] <= 152 and 157 <= numClickPos[1] <= 203:
        userRow = 3
        userCol = 2  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 32  #32
        return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    
    elif 6 <= numClickPos[0] <= 50 and 208 <= numClickPos[1] <= 256:
        userRow = 4
        userCol = 0
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 40
        return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)   
    elif 56 <= numClickPos[0] <= 103 and 208 <= numClickPos[1] <= 256:
        userRow = 4
        userCol = 1  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 41
        return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)   
    elif 107 <= numClickPos[0] <= 152 and 208 <= numClickPos[1] <= 256:
        userRow = 4
        userCol = 2  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 42
        return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    
    elif 6 <= numClickPos[0] <= 50 and 259 <= numClickPos[1] <= 303:
        userRow = 5
        userCol = 0
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 50
        return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 56 <= numClickPos[0] <= 103 and 259 <= numClickPos[1] <= 303:
        userRow = 5
        userCol = 1  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 51
        return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)   
    elif 106 <= numClickPos[0] <= 152 and 259 <= numClickPos[1] <= 303:
        userRow = 5
        userCol = 2  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 52
        return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)

    #FIFTH SUB-GRID (MID-MID)
    elif 158 <= numClickPos[0] <= 206 and 157 <= numClickPos[1] <= 205:
        userRow = 3
        userCol = 3
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 33  
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 208 <= numClickPos[0] <= 257 and 157 <= numClickPos[1] <= 205:
        userRow = 3
        userCol = 4
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 34  
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 259 <= numClickPos[0] <= 305 and 157 <= numClickPos[1] <= 205:
        userRow = 3
        userCol = 5
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 35  
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)

    elif 158 <= numClickPos[0] <= 206 and 209 <= numClickPos[1] <= 255:
        userRow = 4
        userCol = 3
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 43  
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 208 <= numClickPos[0] <= 257 and 209 <= numClickPos[1] <= 255:
        userRow = 4
        userCol = 4
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 44  
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 259 <= numClickPos[0] <= 305 and 209 <= numClickPos[1] <= 255:
        userRow = 4
        userCol = 5
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 45  
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)

    elif 158 <= numClickPos[0] <= 206 and 260 <= numClickPos[1] <= 303:
        userRow = 5
        userCol = 3
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 53  
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 208 <= numClickPos[0] <= 257 and 260 <= numClickPos[1] <= 303:
        userRow = 5
        userCol = 4
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 54  
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 259 <= numClickPos[0] <= 305 and 260 <= numClickPos[1] <= 303:
        userRow = 5
        userCol = 5
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 55  
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)

    #SIXTH SUB-GRID (MID-RIGHT)
    elif 310 <= numClickPos[0] <= 358 and 157 <= numClickPos[1] <= 205: 
        userRow = 3
        userCol = 6  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 36 
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 360 <= numClickPos[0] <= 408 and 157 <= numClickPos[1] <= 205:
        userRow = 3
        userCol = 7
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 37  
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 414 <= numClickPos[0] <= 457 and 157 <= numClickPos[1] <= 205:
        userRow = 3
        userCol = 8
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 38  #08
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    
    elif 310 <= numClickPos[0] <= 358 and 210 <= numClickPos[1] <= 255:  
        userRow = 4
        userCol = 6  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 46
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 360 <= numClickPos[0] <= 408 and 210 <= numClickPos[1] <= 255:
        userRow = 4
        userCol = 7
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 47
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 414 <= numClickPos[0] <= 457 and 210 <= numClickPos[1] <= 255:
        userRow = 4
        userCol = 8
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 48
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)

    elif ((length/9)*6) <= numClickPos[0] <= ((length/9)*7) and ((length/9)*5) <= numClickPos[1] <= ((length/9)*6):  
        userRow = 5
        userCol = 6  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 56
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif ((length/9)*7)+1 <= numClickPos[0] <= ((length/9)*8) and ((length/9)*5) <= numClickPos[1] <= ((length/9)*6): 
        userRow = 5
        userCol = 7
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 57
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif ((length/9)*8)+1 <= numClickPos[0] <= ((length/9)*9) and ((length/9)*5) <= numClickPos[1] <= ((length/9)*6): 
        userRow = 5
        userCol = 8
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 58
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)

    #SEVENTH SUB-GRID (BOTT-LEFT)
    elif 6 <= numClickPos[0] <= 50 and 310 <= numClickPos[1] <= 355:  
        userRow = 6
        userCol = 0  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 60 
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 57 <= numClickPos[0] <= 102 and 310 <= numClickPos[1] <= 355:
        userRow = 6
        userCol = 1
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 61  #31
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 107 <= numClickPos[0] <= 152 and 310 <= numClickPos[1] <= 355:
        userRow = 6
        userCol = 2  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 62  #32
        return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    
    elif 6 <= numClickPos[0] <= 50 and 363 <= numClickPos[1] <= 405:
        userRow = 7
        userCol = 0
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 70
        return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)   
    elif 56 <= numClickPos[0] <= 103 and 363 <= numClickPos[1] <= 405:
        userRow = 7
        userCol = 1  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 71
        return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)   
    elif 107 <= numClickPos[0] <= 152 and 363 <= numClickPos[1] <= 405:
        userRow = 7
        userCol = 2  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 72
        return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    
    elif 6 <= numClickPos[0] <= 50 and 414 <= numClickPos[1] <= 457:
        userRow = 8
        userCol = 0
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 80
        return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 56 <= numClickPos[0] <= 103 and 414 <= numClickPos[1] <= 457:
        userRow = 8
        userCol = 1  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 81
        return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)   
    elif 106 <= numClickPos[0] <= 152 and 414 <= numClickPos[1] <= 457:
        userRow = 8
        userCol = 2  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 82
        return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)

    #EIGHTH SUB-GRID (BOTT-MID)
    elif 158 <= numClickPos[0] <= 206 and 310 <= numClickPos[1] <= 355: 
        userRow = 6
        userCol = 3
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 63  
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 208 <= numClickPos[0] <= 257 and 310 <= numClickPos[1] <= 355: 
        userRow = 6
        userCol = 4
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 64  
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 259 <= numClickPos[0] <= 305 and 310 <= numClickPos[1] <= 355: 
        userRow = 6
        userCol = 5
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 65  
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)

    elif 158 <= numClickPos[0] <= 206 and 363 <= numClickPos[1] <= 405:
        userRow = 7
        userCol = 3
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 73  
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 208 <= numClickPos[0] <= 257 and 363 <= numClickPos[1] <= 405:
        userRow = 7
        userCol = 4
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 74  
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 259 <= numClickPos[0] <= 305 and 363 <= numClickPos[1] <= 405:
        userRow = 7
        userCol = 5
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 75  
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)

    elif 158 <= numClickPos[0] <= 206 and 414 <= numClickPos[1] <= 457:
        userRow = 8
        userCol = 3
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 83  
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 208 <= numClickPos[0] <= 257 and 414 <= numClickPos[1] <= 457:
        userRow = 8
        userCol = 4
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 84  
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 259 <= numClickPos[0] <= 305 and 414 <= numClickPos[1] <= 457:
        userRow = 8
        userCol = 5
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 85  
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)

    #NINTH SUB-GRID (BOTT-RIGHT)
    elif 310 <= numClickPos[0] <= 358 and 310 <= numClickPos[1] <= 355: 
        userRow = 6
        userCol = 6  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 66 
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 360 <= numClickPos[0] <= 408 and 310 <= numClickPos[1] <= 355: 
        userRow = 6
        userCol = 7
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 67  
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 414 <= numClickPos[0] <= 457 and 310 <= numClickPos[1] <= 355: 
        userRow = 6
        userCol = 8
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 68  #08
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    
    elif 310 <= numClickPos[0] <= 358 and 360 <= numClickPos[1] <= 407: 
        userRow = 7
        userCol = 6  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 76
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 360 <= numClickPos[0] <= 408 and 360 <= numClickPos[1] <= 407:
        userRow = 7
        userCol = 7
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 77
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 414 <= numClickPos[0] <= 458 and 360 <= numClickPos[1] <= 407:
        userRow = 7
        userCol = 8
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 78
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)

    elif 310 <= numClickPos[0] <= 358 and 414 <= numClickPos[1] <= 457: 
        userRow = 8
        userCol = 6  
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 86
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 360 <= numClickPos[0] <= 408 and 414 <= numClickPos[1] <= 457:
        userRow = 8
        userCol = 7
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 87
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)
    elif 414 <= numClickPos[0] <= 457 and 414 <= numClickPos[1] <= 457:
        userRow = 8
        userCol = 8
        if ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol) == True:
            return 88
        else:
            return ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol)

    #GRID NOT CLICKED
    else: 
        return 888

def ClickLocationLegal(screen, playingGrid, initialGrid, userNum, userRow, userCol): #playing grid (get both coords)
    if isElementNotGenerated(initialGrid, userCol, userRow) == False:
        return "eThree"
    elif repeatInRow(playingGrid, userNum, userRow) == True and repeatInCol(playingGrid, userNum, userCol) != True:   #check if num in row
        return "eOne"
    elif repeatInRow(playingGrid, userNum, userRow) != True and repeatInCol(playingGrid, userNum, userCol) == True:   #check if num in col
        return "eTwo"
    elif repeatInRow(playingGrid, userNum, userRow) == True and repeatInCol(playingGrid, userNum, userCol) == True:   #check if num in both
        return "eFour"   
    elif repeatinSubGrid(playingGrid, userNum, userRow, userCol) == True: #check subgrid (row, col = legal by now)
        return "eFive"
    return True #if all checks passed, return true - move is legal

def isElementNotGenerated(initialGrid, userCol, userRow):    #inital grid
    if initialGrid[userRow][userCol] != 0:   #is square orginally filled?  
        return False   #yes is was so not allowed

    return True

def repeatinSubGrid(playingGrid, userDigit, userRow, userCol): #playing grid
    if userDigit != 0:
        startRow = userRow - userRow % 3
        startCol = userCol - userCol % 3

        for i in range(3):
            for j in range(3):
                if playingGrid[i + startRow][j + startCol] == userDigit:
                    return True
    return False

def repeatInRow(playingGrid, userDigit, userRow):
    if userDigit != 0:
        for x in range(8):
            if (playingGrid[userRow][x] == userDigit):
                return True
    return False

def repeatInCol(playingGrid, userDigit, userCol):
    if userDigit != 0:
        for x in range(8):
            if (playingGrid[x][userCol] == userDigit):
                return True
    return False

def updateScreen(screen, playingGrid, initialGrid, userRow, userCol, userNum): #draws the grid after each move
    playingGrid[userRow][userCol] = 0 #Erase any previously entered num
    drawG.drawDuringGame(screen, playingGrid, initialGrid, userRow, userCol, 0)  #redraw grid with empty square
    playingGrid[userRow][userCol] = userNum #add new number to square
    drawG.drawDuringGame(screen, playingGrid, initialGrid, userRow, userCol, userNum)  #redraw grid with new number

def getErrPos(coords, userNum):  #getting position of error message
    if coords == 888: #did not click grid   
        if userNum == 0:
            pos = (645, 343)
        else:
            pos = (515, 345)     
    elif coords == "eOne" or coords == "eTwo" or coords == "eThree" or coords == "eFive": #invalid row, col, location  
        pos = (520, 346) 
    elif coords == "eFour": #invalid row and col
        pos = (540, 343) 
    else: #no errors, so don't change position
        pos = (525, 335)  
    return pos

def getErrCmd(coords, userNum): #getting the command to display when there is an error
    if coords == 888: #did not click grid   
        if userNum == 0:
            command = "Click on the number\nyou want to remove."
        else:  
            command = "Please click on the grid or click 'select number'\nto choose another number."
    elif coords == "eOne": #invalid row  
        command = "This row already contains the number " + str(userNum) + ".\nPlease choose another square."
    elif coords == "eTwo": #invalid col 
        command = "This column already contains the number " + str(userNum) + ".\nPlease choose another square."
    elif coords == "eThree": #invalid location   
        command = "You can't change pre-existing numbers.\nPlease choose another square."
    elif coords == "eFour": #invalid row and col   
        command = "This row and column already contain the\nnumber " + str(userNum) + ". Please choose another square."
    elif coords == "eFive": #invalid location   
        command = "The number " + str(userNum) + " is already in this sub-grid.\nPlease choose another square."
    else: #no error
        command = "You have selected the number " + str(userNum) + ".\nSelect grid location or click 'select number'\nto choose another number."
    return command

def noErrorUpdateScreen(coords, screen, playingGrid, initialGrid, userNum):
    userRow = math.trunc(coords/10)  #getting row 
    userCol = int(round(((coords/10)-userRow)*10))  #getting column 
    turn = 2 #change turn so now user needs to select a number

    updateScreen(screen, playingGrid, initialGrid, userRow, userCol, userNum)

    return turn
