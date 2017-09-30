#include <stdio.h>

/*
void print_boolean(int x, int y)
{
	if (x > 0 && y < 10)
		printf("%d in of range.\n", x);
	else
		printf("%d out of range.\n", x);
}

int main(void)
{
	print_boolean(5, 12);
	return 0;
}
*/

void print_boolean(int x, int y)
{
	if (x < 0 || y > 10)
		printf("%d in of range.\n", x);
	else
		printf("%d out of range.\n", x);
}

int main(void)
{
	print_boolean(5, 12);
	return 0;
}

/*
void print_boolean(int x, int y)
{
	if (x <= 0 && y <= 0)
		printf("Test failed.\n");
	else
		printf("Test OK.\n");
}

int main(void)
{
	print_boolean(5, 7);
	return 0;
}
*/
