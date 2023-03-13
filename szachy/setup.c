#include <stdio.h>


int main(void){
    int board[8][8] = {
        8, 11, 12, 12, 12, 12, 5, 2,
        10, 11, 12, 12, 12, 12, 5, 4,
        9, 11, 12, 12, 12, 12, 5, 3,
        6, 11, 12, 12, 12, 12, 5, 0,
        7, 11, 12, 12, 12, 12, 5, 1,
        9, 11, 12, 12, 12, 12, 5, 3,
        10, 11, 12, 12, 12, 12, 5, 4,
        8, 11, 12, 12, 12, 12, 5, 2
    };    

    FILE *ruchy;
    ruchy = fopen("./ruchy.txt", "w");

    if (ruchy==NULL){
        printf("Blad w trakcie otwierania pliku");
        return -1;
    }
    for(int i=0; i<8; i++){
        for(int j=0; j<8; j++){
            fprintf(ruchy, "%d ", board[i][j]);
        }
    }
    fclose(ruchy);
    return 0;
}