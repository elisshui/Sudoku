import pygame

class displaySettings(): #stores screen display settings
    def __init__(self):
        self.screenWidth = 1000
        self.screenHeight = 465
        self.bgColor = (173, 216, 230)

    def createDisplay(self):
        pygame.init() #initialization
        display = pygame.display.set_mode((self.screenWidth, self.screenHeight)) #set display size
        display.fill(self.bgColor) #set background color
        pygame.display.set_caption("Sudoku") #set name of window

        return display

