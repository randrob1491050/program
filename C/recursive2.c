#include <stdio.h>

int fib(int n) {
	if(0 == n) {
		return 1;
	}
	if(1 == n) {
		return 1;
	}
	else {
		return fib(n - 1) + fib(n - 2);
	}
}

int main(void) {
	int num = 0, result = 0;
	printf("Input number:\n");
	scanf("%d", &num);
	result = fib(num);
	printf("The Fibonacci of n is %d\n", result);
}
