#include <stdio.h>

void print_modulo(int x)
{
	printf("tens digit: %d and single digit: %d\n", x/10, x%10);
}

int main(void)
{
	print_modulo(21);
	return 0;
}
