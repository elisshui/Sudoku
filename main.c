#include "Generator.h"
#include "playMode.h"

int main() {
    int generatedGrid[9][9]; //the orginal grid
    linearFill(generatedGrid); //fill the grid with numbers
    getLevel(generatedGrid); //get level of difficulty and remove numbers
    playing(generatedGrid); //runs game and will print the updated grid after each move
  
    return 0;
}
