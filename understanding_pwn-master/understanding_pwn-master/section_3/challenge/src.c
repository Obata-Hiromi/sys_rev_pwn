#include <stdio.h>
#include <stdlib.h>

void win() {
    system("sh");
}

int main() {
    int zero = 0;
    char name[30];
    printf("What's your name?\n>");
    scanf("%s", name);
    if (zero != 0) {
        win();
    }
    printf("hello %s!\n", name);
}
