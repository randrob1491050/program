#include <stdio.h>

int gcd(int a, int b) {
	if(0 == a % b) {
		return b;
	}
	else {
		return gcd(b, a % b);
	}
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
