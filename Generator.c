#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include "Generator.h"

void linearFill(int grid[9][9]){
    int availableNum[numOfBlocks][sudDimension];
    initialAvailable(availableNum);
    int numIndex;
    int rowIndex;
    int colIndex;
    int currPosition = 0;
    srand(time(NULL));
    while (currPosition < 81)
    {      
        if(outOfNumber(currPosition, availableNum) && currPosition > 0){
            replenishSquareNum(currPosition, availableNum);
            grid[rowIndex][colIndex] = 0;
            currPosition--; //back one square

        }

        //get a random number from available list
        do
        {
            numIndex = rand() % 9;
        } while (availableNum[currPosition][numIndex] == 0);
        rowIndex = currPosition / 9;
        colIndex = currPosition % 9;
        //check any conflict
        if(checkMoveLegal(grid, availableNum[currPosition][numIndex], rowIndex, colIndex)) {
            grid[rowIndex][colIndex] = availableNum[currPosition][numIndex];
        } else{
            availableNum[currPosition][numIndex] = 0;
            continue;
        }
        currPosition++;
    }
}

void initialAvailable(int availArray[81][9]){
    for (int i = 0; i < 81; i++){
        for (int j = 0; j < 9; j++){
            availArray[i][j] = j + 1; //fill in 1 - 9 in 0-8
        }
    }
}

bool outOfNumber(int indexAvail, int availArr[81][9]){
    for (int i = 0; i < 9; i++){
        if (availArr[indexAvail][i] != 0){
            return false;
        }
    }
    return true;
}

void replenishSquareNum(int index, int arrayAvail[81][9]){
    for (int i = 0; i < 9; i++){
        arrayAvail[index][i] = i + 1;
    }
}

bool repeatinSubGrid(int grid[9][9], int userDigit, int userRow, int userCol){
    int startRow = userRow - userRow % 3, startCol = userCol - userCol % 3;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (grid[i + startRow][j + startCol] == userDigit)
                return true;
    return false;
}
bool repeatInRow(int grid[9][9], int userDigit, int userRow){
    for (int x = 0; x <= 8; x++)
        if (grid[userRow][x] == userDigit)
            return true;
    return false;
}
bool repeatInCol(int grid[9][9], int userDigit, int userCol){
    for (int x = 0; x <= 8; x++)
        if (grid[x][userCol] == userDigit)
            return true;
    return false;
}

bool checkMoveLegal(int grid[9][9], int userDigit, int userRow, int userCol){
    if (!repeatinSubGrid(grid,userDigit,userRow, userCol)
        &&!repeatInRow(grid,userDigit,userRow)
        &&!repeatInCol(grid,userDigit,userCol)){
        return true;
    }
    else{
        return false;
    }
}

void getLevel(int generatedGrid[9][9]) {
    int difficulty, numRemove;
    bool invalid = false;
    printf("Please select the level of difficulty:\n1 - Easy\n2 - Medium\n3 - Hard.\n");
    do {
        scanf("%d", &difficulty);
        if(difficulty != 1 && difficulty != 2 && difficulty != 3) {
            invalid = true;
            printf("Sorry, that was not an option.\nPlease enter your desired level again: ");
        }
    } while(invalid == true);

    if(difficulty == 1) {
        numRemove = (rand()%(25-17+1))+17;  //random between 15 and 11
    }
    else if(difficulty == 2) {
        numRemove = (rand()%(33-26+1))+26;  //random between 12 and 17
    }     
    else if(difficulty == 3) {
        numRemove = (rand()%(49-34+1))+34;  //random between 18 and 25
    } 
    removeKDigits(numRemove, generatedGrid);
    return;
}

void removeKDigits(int numRemove, int generateGrid[9][9])
{
    time_t t;
    srand((unsigned) time(&t));
    while (numRemove != 0)
    {
        int i = rand()%9;
        int j = rand()%9;
        if (generateGrid[i][j] != 0)
        {
            numRemove--;
            generateGrid[i][j] = 0;
        }
    }
}
