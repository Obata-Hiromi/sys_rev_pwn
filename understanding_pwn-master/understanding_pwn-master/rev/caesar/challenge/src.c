#include <stdio.h>

void main() {
    char s[53] = {102, 109, 99, 106, 127, 126, 54, 124, 103, 109, 58, 121, 128, 108, 118, 67, 134, 68, 113, 135, 68, 116, 120, 74, 119, 92, 78, 78, 143, 80, 144, 126, 148, 81, 129, 152, 146, 137, 89, 153, 155, 157, 94, 153, 144, 140, 113, 99, 99, 164, 102, 165, 177};
    for (int i = 0; i < 53; i++)
        s[i] = s[i] - i;
}

