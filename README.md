<h1>Sudoku</h1>
One of the earliest records of Sudoku comes from 1783 when Leonhard Euler came up with, what he called, "Latin Squares" - a new form of <a href = "https://mathworld.wolfram.com/MagicSquare.html">magic squares</a>. The modern 9-by-9 grid was popularized by Maki Kaji, the owner of Nikoli magazines. I had orginally coded this game in C and utilized the backtracking algorithm to randomly generate a grid each time the game was run. However, I sought to create a more interactive game. Thus, I used Python and its pygame library to re-write the code and create a graphical user interface.<br><br>

<strong>Project Goals:</strong>
* To become proficient in splitting up code into different functions and files.<br>
* To dig deeper into Python's functions.<br><br>

<h2>Game Features</h2>
With the GUI, players can choose to reset the board or view the answer at any point in the game. The game also features a comprehensive set of error-checking functions. So, if the player makes an illegal move, a message explaining why the move was not allowed will be displayed. This is especially helpful if the player is new to the game. The GUI is displayed in the image below.<br><br>
<img src="https://github.com/elisshui/Sudoku/blob/main/startScreen.JPG" alt="Sudoku" width=90%>

<h2>Sudoku Board Algorithm</h2>
As stated, the backtracking algorithm was used to create the Sudoku grid in C. However, when changing the code to Python, I utilized a different algorithm. This is seen in the code block below.<br><br>

```python
import copy
from random import sample

subGridDim = 3 #dimensions of each sub-grid
subGridArea = subGridDim * subGridDim #area of each subgrid

def pattern(r, c): #creating pattern for a baseline valid solution
   return (subGridDim * (r % subGridDim) + r // subGridDim + c) % subGridArea

def shuffle(s): #gets random number of rows, columns and numbers (of valid base pattern)
   return sample(s, len(s)) #randomly shuffled non-repeating numbers from 1-9

rBase = range(subGridDim) #outputs sequence of nums from 0-3
rows = [g * subGridDim + r for g in shuffle(rBase) for r in shuffle(rBase)]
cols = [g * subGridDim + c for g in shuffle(rBase) for c in shuffle(rBase)]
nums = shuffle(range(1, subGridDim*subGridDim+1)) #generates list [1,...9] - get random num from here

#Produce board using randomized pattern
answerGrid = [[nums[pattern(r,c)] for c in cols] for r in rows] #storing the answers
initialGrid = copy.deepcopy(answerGrid) #copy to make playing grid

#-------MAKING SPACES----------
squares = subGridArea * subGridArea #making spaces
numSpace = 44 #number of spaces
for p in sample(range(squares), numSpace): #randomly place spaces
   initialGrid[p // subGridArea][p % subGridArea] = 0
```

The variable <i>numSpace</i> stores the number of spaces to be removed from the randomly generated board. I set this number to be 44. However, an extra feature would be to allow the user to select a level of difficulty then change the value of <i>numSpace</i> accordingly where more spaces are removed for added difficulty.

<h2>Drawing Game Buttons</h2>
The following functions were used to draw the "Reset Game" button in the game. Similar functions were used to draw the other buttons (these are in the gameButtons.py file).<br><br>

```python
def drawResetBut(screen): #drawing the button for selecting numbers
    pygame.draw.rect(screen,
                    consts.BEIGH,
                    (xPosRes, topMarginRes, widthRes, heightRes))

def resetLines(screen): #drawing the number title
   pygame.draw.line(screen, consts.MEDBLUE,
                   (xPosRes, topMarginRes),
                   (xPosRes, topMarginRes+heightRes), 6) #Right vertical
   pygame.draw.line(screen, consts.MEDBLUE,
                   (xPosRes+widthRes, topMarginRes),
                   (xPosRes+widthRes, topMarginRes+heightRes), 6) #left vertical

def addResetBut(screen): #drawing the button on screen
   font = pygame.font.SysFont('Arial', 23)
   drawResetBut(screen) #draw command bar
   writeCommand(screen, "Reset Board", (805, 168), font)
   resetLines(screen)
```

<h2>Error-checking</h2>
Error-checking functions were also implemented. When the player makes an illegal move, a message is displayed in the command bar explaining why their move was illegal. Some of these messages can be seen below.

| Number Already Exists in Column | Attempting to Change Orginal Numbers. | Number Already Exists in Row and Column. | Number Already Exists in Sub-grid. |
|---------------|-----------------|---------------------|-------------------|
|![](https://github.com/elisshui/Sudoku/blob/main/errorCol.JPG) | ![](https://github.com/elisshui/Sudoku/blob/main/errorPreEx.JPG) | ![](https://github.com/elisshui/Sudoku/blob/main/errorRowCol.JPG) | ![](https://github.com/elisshui/Sudoku/blob/main/errorSubGrid.JPG) |
---

Project by [Eliss Hui](https://github.com/elisshui "Eliss Hui") (June 2022)
