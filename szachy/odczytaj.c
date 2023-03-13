#include <stdio.h>


int main(void){
    int board[8][8];
    FILE *ruchy;
    ruchy = fopen("./ruchy.txt", "r");

    if (ruchy==NULL){
        printf("Blad w trakcie otwierania pliku");
        return -1;
    }

    int cos;
    int cos2;
    for (int i=0; i<8; i++){
        for (int j=0; j<8; j++){
            fscanf(ruchy, "%d", &(board[i][j]));
        }
    }
    for (int i=0; i<8; i++){
        for (int j=0; j<8; j++){
            printf("%d ", board[i][j]);
        }
        printf("\n");
    }
    fclose(ruchy);
    return 0;
}