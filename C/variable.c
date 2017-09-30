#include <stdio.h>

int hour = 23, minute = 59;
int x =10;

void print_time(void)
{
	printf("HOUR:MIN:1 = %d:%d\n", hour, minute);
}

int main(void)
{
	int hour = 10,minute = 59;
	print_time();
	printf("HOUR:MIN:2 = %d:%d\n", hour, minute);
	printf("X = %d\n", x);
	return 0;
}	
