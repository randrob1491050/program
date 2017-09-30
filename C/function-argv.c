#include <stdio.h>

void print_time(int hour, int min)
{
	printf("Hour:%d\tMin:%d\n", hour, min);
}

int main(void)
{
	print_time(23, 59);
	return 0;
}

