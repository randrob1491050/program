#include <stdio.h>

/* exp progame */
/* 
 * comment1
 */

int main(void)
{
	int hour;
	int minute;
	hour = 11;
	minute = 59;
	printf("%d hours and %d percent of an hours\n",hour,minute * 100 / 60);
	/* printf("%d and %f hours\n",hour,minute / 60); */
	printf("%d and %f hours\n",hour,minute / 60.0);
	return 0;
}
