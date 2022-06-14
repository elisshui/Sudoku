import pygame
import gameConstants as consts

def drawBar(screen):  #drawing the number title
    pygame.draw.rect(screen,
                    consts.LGTGREEN,
                    (500, 320, 450, 110))

def lines(screen):  #drawing the number title
    pygame.draw.line(screen, consts.MEDBLUE, (500, 320), (500, 430), 6) #Right vertical
    pygame.draw.line(screen, consts.MEDBLUE, (950, 320), (950, 430), 6) #left vertical

def writeCommand(screen, command, pos): #blit command   
    font = pygame.font.SysFont('Arial', 25)

    text = [word.split(' ') for word in command.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
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


def addCommBar(screen, command, pos):  #drawing the grid and title
    drawBar(screen)  #draw command bar
    writeCommand(screen, command, pos)
    lines(screen)