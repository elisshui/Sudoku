import pygame
import gameConstants as consts

def writeCommand(screen, command, pos, font):  #blit command   
    text = [word.split(' ') for word in command.splitlines()]  #2D array where each row is a list of words.
    space = font.size(' ')[0]  #The widthNum of a space.
    max_width, max_height = screen.get_size()
    x, y = pos
    
    for line in text:
        for word in line:
            word_surface = font.render(word, 0, consts.DRKGRAY)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            screen.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

#------------------------Select Number Button-----------------------------
xPosNum = 775
topMarginNum = 27
widthNum = 160
heightNum = 50

def drawSelNumBut(screen):  #drawing the button for selecting numbers
    pygame.draw.rect(screen,
                    consts.LGHYELLOW,
                    (xPosNum, topMarginNum, widthNum, heightNum))

def SelNumLines(screen):  #drawing the number title
    pygame.draw.line(screen, consts.MEDBLUE,
                    (xPosNum, topMarginNum),
                    (xPosNum, topMarginNum+heightNum), 6) #Right vertical
    pygame.draw.line(screen, consts.MEDBLUE,
                    (xPosNum+widthNum, topMarginNum),
                    (xPosNum+widthNum, topMarginNum+heightNum), 6) #left vertical

def addSelNumBut(screen):  #drawing the button on screen
    font = pygame.font.SysFont('Arial', 23)
    drawSelNumBut(screen)  #draw command bar
    writeCommand(screen, "Select Number", (795, 38), font)
    SelNumLines(screen)

    pygame.display.flip()  #update screen

#------------------------Remove Numbers Button-----------------------------
xRevNum = 775
topRevNum = 87
widthRevNums = 160
heightRevNum = 60

def drawRevNumBut(screen):  #drawing the button for selecting location on grid
    pygame.draw.rect(screen,
                    consts.LGHYELLOW,
                    (xRevNum, topRevNum, widthRevNums, heightRevNum))

def revNumLines(screen):  #drawing the number title
    pygame.draw.line(screen, consts.MEDBLUE, (xRevNum, topRevNum), (xRevNum, topRevNum+heightRevNum), 6) #Right vertical
    pygame.draw.line(screen, consts.MEDBLUE,
                    (xRevNum+widthRevNums, topRevNum),
                    (xRevNum+widthRevNums, topRevNum+heightRevNum), 6)

def addRevNumBut(screen):  #drawing the button on screen
    font = pygame.font.SysFont('Arial', 21)
    drawRevNumBut(screen)  #draw command bar
    writeCommand(screen, "Remove a number\n       on the grid", (783, 91), font)
    revNumLines(screen)

    pygame.display.flip()  #update screen

#------------------------Reset Game Button-----------------------------
xPosRes = 775
topMarginRes = 157
widthRes = 160
heightRes = 50

def drawResetBut(screen):  #drawing the button for selecting numbers
    pygame.draw.rect(screen,
                    consts.BEIGH,
                    (xPosRes, topMarginRes, widthRes, heightRes))

def resetLines(screen):  #drawing the number title
    pygame.draw.line(screen, consts.MEDBLUE,
                    (xPosRes, topMarginRes),
                    (xPosRes, topMarginRes+heightRes), 6) #Right vertical
    pygame.draw.line(screen, consts.MEDBLUE,
                    (xPosRes+widthRes, topMarginRes),
                    (xPosRes+widthRes, topMarginRes+heightRes), 6) #left vertical

def addResetBut(screen):  #drawing the button on screen
    font = pygame.font.SysFont('Arial', 23)
    drawResetBut(screen)  #draw command bar
    writeCommand(screen, "Reset Board", (805, 168), font)
    resetLines(screen)

    pygame.display.flip()  #update screen

#------------------------Show Answers Button-----------------------------
xPosAns = 775
topMarginAns = 217
widthAns = 160
heightAns = 50

def drawAnsBut(screen):  #drawing the button for selecting numbers
    pygame.draw.rect(screen,
                    consts.LGHORANGE,
                    (xPosAns, topMarginAns, widthAns, heightAns))

def ansLines(screen):  #drawing the number title
    pygame.draw.line(screen, consts.MEDBLUE,
                    (xPosAns, topMarginAns),
                    (xPosAns, topMarginAns+heightAns), 6) #Right vertical
    pygame.draw.line(screen, consts.MEDBLUE,
                    (xPosAns+widthAns, topMarginAns),
                    (xPosAns+widthAns, topMarginAns+heightAns), 6) #left vertical

def addAnsBut(screen):  #drawing the button on screen
    font = pygame.font.SysFont('Arial', 23)
    drawAnsBut(screen)  #draw command bar
    writeCommand(screen, "Answers", (820, 227), font)
    ansLines(screen)

    pygame.display.flip()  #update screen