import pygame
import gameConstants as consts

def gridStruct(initialGrid):
        for row in range(9): #creating a 2D array (a list of lists)
            initialGrid.append([]) #per row add empty array
            for column in range(9):
                initialGrid[row].append(0)  #append a cell

def drawLines(screen): #draw grid lines
    color = consts.MEDBLUE
    pygame.draw.line(screen, color, (2, 2), (2, 460), 6) #Right vertical
    pygame.draw.line(screen, color, (153, 4), (153, 457), 6) #Mid Left vertical
    pygame.draw.line(screen, color, (((457/3)*2)+3, 4), (((457/3)*2)+3, 457), 6) #Mid Right vertical
    pygame.draw.line(screen, color, (458, 2), (458, 458), 6) #Left vertical

    pygame.draw.line(screen, color, (4, 4), (457, 4), 6) #Top horizontal
    pygame.draw.line(screen, color, (4, 153), (457, 153), 6) #Mid Top horizontal
    pygame.draw.line(screen, color, (4, ((457/3)*2)+3), (457, ((457/3)*2)+3), 6) #Mid Bottom horizontal
    pygame.draw.line(screen, color, (2, 460), (460, 460), 6) #Bottom horizontal


def drawOriginal(screen, column, row):  #drawing the squares that are initially filled
    margin = 5
    size = 46
    pygame.draw.rect(screen,
                    consts.LGTGREEN,
                    [(margin + size) * column + margin,
                    (margin + size) * row + margin,
                    size,
                    size])

def drawUnoccInGame(screen, column, row):  #drawing the unoccupied squares
    margin = 5
    size = 46
    pygame.draw.rect(screen,
                    consts.LGHGRAY,
                    [(margin + size) * column + margin,
                    (margin + size) * row + margin,
                    size,
                    size])

def writeNums(screen, row, column, grid):   #putting orginal numbers on screen
    margin = 5
    size = 46 
    fontOrgNums = pygame.font.SysFont('arial', 37)
    text = fontOrgNums.render(str(grid[row][column]), True, consts.DRKGRAY)
    textCenter = text.get_rect(center = ((((margin + size) * column + margin)+22), (((margin + size) * row + margin)+23))) 
    screen.blit(text, textCenter)

def writeNewNum(screen, row, column, num):   #putting orginal numbers on screen
    margin = 5
    size = 46 
    fontOrgNums = pygame.font.SysFont('arial', 37)
    text = fontOrgNums.render(str(num), True, consts.DRKGRAY)
    textCenter = text.get_rect(center = ((((margin + size) * column + margin)+22), (((margin + size) * row + margin)+23))) 
    screen.blit(text, textCenter)

def drawGameStart(screen, initialGrid):  #drawing the grid (before game starts)
    for row in range(9):  
        for column in range(9):
            if initialGrid[row][column] != 0: #if occupied originally, change color, put number
                drawOriginal(screen, column, row)
                writeNums(screen, row, column, initialGrid) #puts original numbers on
            else: #unoccupied 
                drawUnoccInGame(screen, column, row)
    drawLines(screen)
    pygame.display.flip()  #update screen

def drawDuringGame(screen, playingGrid, initialGrid, userRow, userCol, num):  #drawing the grid during the game
    for row in range(9):  
        for column in range(9):
            if initialGrid[row][column] != 0: #if occupied originally, change color.
                drawOriginal(screen, column, row) #change color of orginal
                writeNums(screen, row, column, initialGrid)
            elif playingGrid[row][column] == 0:  #unoccupied 
                drawUnoccInGame(screen, column, row)

    if playingGrid[userRow][userCol] != 0: 
        writeNewNum(screen, userRow, userCol, num) #adding new number to playing grid

    drawLines(screen)

def drawAnswer(screen, answerGrid, initialGrid):  #shows the answers
    for row in range(9):  
        for column in range(9):
            if initialGrid[row][column] != 0: #if occupied originally, change color, put number
                drawOriginal(screen, column, row)
                writeNums(screen, row, column, answerGrid) #puts original numbers on
            else: #unoccupied 
                drawUnoccInGame(screen, column, row)
                writeNums(screen, row, column, answerGrid) #puts original numbers on
    drawLines(screen)
    pygame.display.flip()  #update screen
    