#ifndef _playMode_h_
#define _playMode_h_
#include <stdbool.h>
#define sudDimension 9
#define numOfBlocks 81

/*Checks if all the spaces in the grid are taken up and returns to user if it is*/
bool gameOver(int grid[sudDimension][sudDimension]);

/* This function takes in the user’s selected row and column to check whether the position has an element.
* Return type: boolean
* Parameter: the integer which represents the user's choice on row and column
*/
bool isElementNotGenerated(int generatedGrid[sudDimension][sudDimension],int userCol, int userRow);

/*
* Prints the grid to the console, takes the grid as an input.
* Return Type: void
* Parameter: the playing grid
*/
void printSudokuGrid(int grid[sudDimension][sudDimension]);

/*
* Runs the actual game.
* Return Type: void
* Parameter: the initially generated grid
*/
void playing(int generatedGrid[9][9]);

/*
* Gets the user's input (number). Completes error checking.
* Return Type: boolean
* Parameter: pointer to the user's number entered
*/
bool getNumber(int *);

/*
* Gets the user's input (row coordinates). Completes error checking.
* Return Type: boolean
* Parameter: pointer to the user's row coordinates
*/
bool getRowCoord(int grid[9][9], int userNum, int *userRow);

/*
* Gets the user's input (column coordinates). Completes error checking.
* Return Type: boolean
* Parameter: pointer to the user's column coordinates
*/
bool getColCoord(int grid[9][9], int userNum, int *userCol);

/*
* Checks the overall validity (sub-grid repeats and location on board) of the user's move.
* Return Type: integer
* Parameter: playing grid, the orginal grid, the number inputted, the inputted coordinates.
*/
int validMoveCheck(int grid[9][9], int generatedGrid[9][9], int userNum, int userCol, int userRow);

#endif
