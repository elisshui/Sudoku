import pygame
import gameConstants as consts

numpadNums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def numpadStruct(): #create the structure for the number pad
        for row in range(3):
            numpadNums.append([])
            for column in range(3):
                numpadNums[row].append(0)  # Append a cell

def drawPad(screen, column, row):  #drawing the number pad itself
    margin = 5
    size = 70
    pygame.draw.rect(screen,
                    consts.LGTGREEN,
                    [(margin + size) * column + 500,
                    (margin + size) * row + 80,
                    size,
                    size])

def drawTitle(screen):  #drawing the number title
    pygame.draw.rect(screen,
                    consts.LGTGREEN,
                    (500, 20, 220, 50))

def lines(screen):  #drawing the number title
    pygame.draw.line(screen, consts.MEDBLUE, (500, 20), (500, 300), 6) #Right vertical
    pygame.draw.line(screen, consts.MEDBLUE, (720, 20), (720, 300), 6) #left vertical

def writeNums(screen, row, column, numpadNums):   #putting number pad numbers on screen
    margin = 5
    size = 70 
    fontOrgNums = pygame.font.SysFont('arial', 37)
    text = fontOrgNums.render(str(numpadNums[row][column]), True, consts.DRKGRAY)
    textCenter = text.get_rect(center = ((((margin + size) * column + 534)), (((margin + size) * row + 115)))) 
    screen.blit(text, textCenter)

def writePadTitle(screen):   #putting title of number pad on screen
    fontOrgNums = pygame.font.SysFont('arial', 37)
    text = fontOrgNums.render(str("Number Pad"), True, consts.DRKGRAY)
    textCenter = text.get_rect(center = (610, 44)) 
    screen.blit(text, textCenter)

def addNumPad(screen):  #drawing the grid and title
    for row in range(3):  
        for column in range(3):
            drawPad(screen, column, row)  #number pad structure
            drawTitle(screen) #title bar structure
            writePadTitle(screen) #write title in bar
            writeNums(screen, row, column, numpadNums) #write numbers on pad
            lines(screen)

    pygame.display.flip()  #update screen