import copy
from random import sample

subGridDim = 3  #dimensions of each sub-grid
subGridArea = subGridDim*subGridDim  #area of each subgrid

def pattern(r, c):   #creating pattern for a baseline valid solution
    return (subGridDim * (r % subGridDim) + r // subGridDim + c) % subGridArea

def shuffle(s):  #gets random number of rows, columns and numbers (of valid base pattern)
    return sample(s, len(s)) #randomly shuffled non-repeating numbers from 1-9

rBase = range(subGridDim) #outputs sequence of nums from 0-3
rows  = [g*subGridDim + r for g in shuffle(rBase) for r in shuffle(rBase)] 
cols  = [g*subGridDim + c for g in shuffle(rBase) for c in shuffle(rBase)]
nums  = shuffle(range(1, subGridDim*subGridDim+1)) #generates list [1,...9] - get random num from here

# produce board using randomized pattern
answerGrid = [[nums[pattern(r,c)] for c in cols] for r in rows]  #storing the answers
initialGrid = copy.deepcopy(answerGrid)  #copy to make playing grid

#-------MAKING SPACES----------
squares = subGridArea*subGridArea  #making spaces
numSpace = 1 #number of spaces
for p in sample(range(squares), numSpace): #randomly place spaces
    initialGrid[p // subGridArea][p % subGridArea] = 0
