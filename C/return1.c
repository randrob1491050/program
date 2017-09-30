#include <stdio.h>


int is_leap_year(int year)
{
	if (( year % 4 == 0 && year % 100 != 0 ) || year % 400 == 0 )
		printf("%d is leap yeah\n", year);
	else
		printf("%d not leap yeah\n", year);
}
		
int main(void)
{
	int year;
	printf("Enter a year: \n");
	scanf("%d", &year);
	is_leap_year(year);
	return 0;
}

