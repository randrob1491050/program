#include <stdio.h>

int gcd(int a, int b)
{
    int temp;
    while (a % b != 0) {
        temp = a % b;
        a = b;
        b = temp;
    }
    return b;
}

int main(void) {
        int x, y, result;
        printf("Input a number:\n");
        scanf("%d", &x);
        printf("Input b number:\n");
        scanf("%d", &y);
        result = gcd(x, y);
        printf("The greatest common divisor is %d\n", result);
}
