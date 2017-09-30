#include <stdio.h>
#include <math.h>

double myround(double x)
{
	if (x >= 0)
	{
		return floor(x + 0.5);
	}
	else
		return ceil(x - 0.5);
}

void main()
{
	double x;
	printf("Input a number:");
	scanf("%lf", &x);
	printf("%lf\n", myround(x));
}
