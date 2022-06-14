import sys
import pygame
import copy
from displaySettings import displaySettings #importing game screen settings from the file called displaySettings
import sudokuGrid as sg #generates inital sudoku board
import drawGrid as drawG #draws the generated grid on the board
import drawNumpad as drawNP #draws the number pad
import drawComBar as drawCB #draws the command bar
import makeMove as playGame #to play the actual game
import gameButtons as drawBtns #draws the buttons

def main():
    disp = displaySettings() #creating instance (the display itself)
    screen = disp.createDisplay() #creating it...
  
    initialGrid = sg.initialGrid  #initial grid with numbers (doesn't change during game)
    playingGrid = copy.deepcopy(initialGrid)  #this grid will be played on
    answerGrid = sg.answerGrid #the answers
    drawG.gridStruct(initialGrid) #creating the grid structure
    drawNP.numpadStruct() #creating the number pad structure
    drawG.drawGameStart(screen, initialGrid) #display board

    pos = (535, 340) #position of command when blitted
    command = "                        Welcome!\nClick on the 'select number' button to start!"  #welcome message
    turn = 0  #used to change functionality
    play = True

    while play == True:
        drawNP.addNumPad(screen) #draw number pad
        drawCB.addCommBar(screen, command, pos) #command bar
        drawBtns.addSelNumBut(screen)  #select num button
        drawBtns.addRevNumBut(screen)  #remove num button
        drawBtns.addResetBut(screen)  #reset board button
        drawBtns.addAnsBut(screen) #answers button

        if playGame.gameOver(playingGrid) == True:
            pos = (580, 343)
            command = "            Congratulations!\nYou have completed the game!"

        for event in pygame.event.get(): #getting user inputs (events)
            if event.type == pygame.QUIT: #when 'x' clicked, exit
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                #------buttons-------
                if (drawBtns.xPosNum <= mousePos[0] <= (drawBtns.xPosNum + drawBtns.widthNum)
                    and drawBtns.topMarginNum <= mousePos[1] <= (drawBtns.topMarginNum + drawBtns.heightNum)): #if clicked, allow user to choose number (starting point)
                    pos = (660, 356)
                    command = "Select a number!"
                    turn = 2
                    
                if (drawBtns.xRevNum <= mousePos[0] <= (drawBtns.xRevNum + drawBtns.widthRevNums)
                    and drawBtns.topRevNum <= mousePos[1] <= (drawBtns.topRevNum + drawBtns.heightRevNum)): #if clicked, remove number
                    userNum = 0
                    turn =  3

                if (drawBtns.xPosRes <= mousePos[0] <= (drawBtns.xPosRes + drawBtns.widthRes)
                    and drawBtns.topMarginRes <= mousePos[1] <= (drawBtns.topMarginRes + drawBtns.heightRes)): #if clicked, reset game
                    playingGrid = copy.deepcopy(initialGrid)  #reset whole board
                    pos = (624, 344)
                    command = "Game sucessfully reset.\n     Select a number!"
                    turn = 2
                    drawG.drawGameStart(screen, initialGrid)  #display board

                if (drawBtns.xPosAns <= mousePos[0] <= (drawBtns.xPosAns + drawBtns.widthAns)
                    and drawBtns.topMarginAns <= mousePos[1] <= (drawBtns.topMarginAns + drawBtns.heightAns)): #if clicked, show answers
                    pos = (664, 358)
                    command = "Answers shown."
                    drawG.drawAnswer(screen, answerGrid, initialGrid)  #draw answers on screen

                #-----game-------
                if turn != 0 and turn%2 == 0:                
                    userNum = playGame.getNumber()                                
                    if userNum != False:
                        pos = (525, 335) 
                        command = "You have selected the number " + str(userNum) + ".\nSelect grid location or click 'select number'\nto choose another number."
                        turn = turn + 1 #change turn to 3
                
                elif turn >= 3 and turn%2 == 1: #Get coords from user
                    coords = playGame.getCoords(screen, playingGrid, initialGrid, userNum)  #getting coords in form rowcol

                    if type(coords) != type(1) or coords == 888: #move not valid
                        command = playGame.getErrCmd(coords, userNum) #display message
                        pos = playGame.getErrPos(coords, userNum) #position message
                         
                    else: #move valid
                        pos = (660, 356) #position message
                        command = "Select a number!" #prompt to select next number
                        turn = playGame.noErrorUpdateScreen(coords, screen, playingGrid, initialGrid, userNum) #change function

    pygame.display.flip()  #update screen

main() #run game - main function
