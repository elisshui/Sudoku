#include "playMode.h"
#include "Generator.h"
#include <stdio.h>
#include <stdlib.h>

bool gameOver(int grid[sudDimension][sudDimension]) {
    for(int r = 0; r < 9; r++) {
        for(int c = 0; c < 9; c++) {
            if(grid[r][c] == 0) {
                return false; //still got an empty space
            }
        }
    }
    return true; //no more spaces
}

void printSudokuGrid(int grid[sudDimension][sudDimension]) {
    printf("+-----------+  +-----------+  +-----------+");
    printf("\n");
    for(int r = 0; r < 9; r++) {
        printf("|");
        for(int c = 0; c < 9; c++) {  //vertical spaces
            printf("%2d |", grid[r][c]);
            if(c==2 || c==5) {
                printf("  |");
            }
        }
        if(r == 2 || r == 5) {  //horizontal spaces
            printf("\n");
            printf("+-----------+  +-----------+  +-----------+");
            printf("\n");
        }
        printf("\n");
        if(r == 8 || r == 5 || r == 2) {
            printf("+-----------+  +-----------+  +-----------+");          
        } else {
            printf("-------------  -------------  -------------");
        }
        printf("\n");
    }
    return;
}

bool getNumber(int *userNum) {
  bool invalid;
  printf("What number would you like to enter? "); //inital prompt
  do {
    invalid = false;
    scanf("%d", userNum);
    if(*userNum < 1 || *userNum > 9) {  //check if in range
      invalid = true;
      printf("\nInvalid number.\nPlease enter another number between 1 and 9 inclusive: ");
    }
  } while(invalid == true);
  return true;
}

bool getRowCoord(int grid[9][9], int userNum, int *userRow) {
  bool invalid;
  printf("\nRow coordinate: "); //inital prompt
  do {
    invalid = false;
    scanf("%d", userRow);
    *userRow = *userRow - 1; //adjust coord
    if(*userRow < 0 || *userRow > 8) {  //check if in range
      invalid = true;
      printf("\nInvalid number.\nPlease enter another number between 1 and 9 inclusive: ");

    }
    else if(repeatInRow(grid, userNum, *userRow)) { //check if num exsits
      invalid = true;
      printf("\nThis row already contains the number %d.\n", userNum);
      printf("Please enter another row coordinate: ");
    }
  } while(invalid == true);
  return true;
}

bool getColCoord(int grid[9][9], int userNum, int *userCol) {
  bool invalid;
  printf("\nColumn coordinate: "); //inital prompt
  do {
    invalid = false;
    scanf("%d", userCol);
    *userCol = *userCol - 1; //adjust coord
    if(*userCol < 0 || *userCol > 8) {  //check if in range
      printf("\nInvalid number.\nPlease enter another number between 1 and 9 inclusive: ");
      invalid = true;
    }
    else if(repeatInCol(grid, userNum, *userCol)) { //check if num exsits
      invalid = true;
      printf("\nThis column already contains the number %d.\n", userNum);
      printf("Please enter another column coordinate: ");
    }
  } while(invalid == true);
  return true;
}

bool checkSubGrid(int grid[9][9], int userNum, int userRow, int userCol) {
  if(repeatinSubGrid(grid, userNum, userRow, userCol)) {
    printf("\nThe number %d is already in the square.\n", userNum);
    return false;
  }
  return true;
}

bool isElementNotGenerated(int generatedGrid[sudDimension][sudDimension],int userCol, int userRow) { //see if position is pre-filled
    if(generatedGrid[userRow][userCol] != 0){ //is square empty?
      printf("\nYou can't change the pre-existing numbers.\n");  
      return false;  //no, it isn't empty
    }
    return true;
}

int validMoveCheck(int grid[9][9], int generatedGrid[9][9], int userNum, int userCol, int userRow) {
  if(getNumber(&userNum) && getRowCoord(grid, userNum, &userRow) && getColCoord(grid, userNum, &userCol) && isElementNotGenerated(generatedGrid, userCol, userRow) && checkSubGrid(grid, userNum, userRow, userCol)) {
    return 1; //legal move
  }
  return 0; //illegal move
}

void playing(int generatedGrid[9][9]) {
  int userNum, userCol, userRow, stepToTake;
  bool invalid;
  int grid[sudDimension][sudDimension];

  for(int r = 0; r < sudDimension; r++) {  //creating board
    for(int c = 0; c < sudDimension; c++) {
      grid[r][c]=generatedGrid[r][c]; //generated grid won't change
    }
  }
  
  printf("To play, enter the number you want to input and your desired coordinates. The number and coordinates must be a number between 1 and 9. Press '0' to re-enter a move and 'E' to exit the game.\n");
  printSudokuGrid(generatedGrid); //print intial board
  while(gameOver(grid) == false) { //while not over, play game
    do { //get input
      invalid = true;
      stepToTake = validMoveCheck(grid, generatedGrid, userNum, userCol, userRow); //get step
      if(stepToTake == 2) { //exit game
        printf("Exiting Game.");
        return;
      }
      else if(stepToTake == 1) { //final legality check
        invalid = false;  
        grid[userRow][userCol] = userNum;
        printSudokuGrid(grid);
      }
      else if(stepToTake == 0) {  //invalid so repeat
        printf("Please enter another move.\n");
        invalid = true;
      }
    } while(invalid == true);
  }
  return;
}
