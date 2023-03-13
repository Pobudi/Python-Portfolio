#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(){
    char run[] = "python szachy_gui.py&";
    char stop[] = "ps | grep python | cut -d \" \" -f3 |xargs kill -SIGKILL";
    char komp[] = "gcc szachy2.c -o wynik; ./wynik";
    char setup[] = "gcc setup.c -o setup; ./setup";

    system(setup);
    while (1){
        system(komp);
        system(run);
        sleep(7);
        system(stop);
    }
    return 0;
}
