#include <stdio.h>

void increment(int x)
{
	x = x + 1;
	printf("Totle:%d\n",x);
}

int main(void)
{
	int i = 1, j = 2;
	increment(i);
	increment(j);
	return 0;
}
