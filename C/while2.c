#include <stdio.h>

int fibonacci(int x)
{
	int temp ;
	if(x == 0||x == 1)
	{
		return 1 ;
	}
	else
	{
		int count1 = 1 ;
		int count2 = 1 ;

		while(x > 1){
		count2 = count1 + count2 ;
		//printf("%d\n", count2) ;
		count1 = count2 - count1 ;
		//printf("%d\n", count1) ;
		x = x - 1 ;
		//printf("%d\n", x) ;
		}
		return count2 ;
	}	
}

int main(void)
{
        int num, result;
        printf("Input numer:\n");
        scanf("%d", &num);
        result = fibonacci(num);
        printf("The Fibonacci of n is %d\n", result);
}

/*
int main(void)
{
	int i ;
	int j ;
	printf("Please input a number.\n") ;
	printf("Number=") ;
	j = scanf("%d", &i) ;
	if(j == 1)
	{
		if(i >= 0)
		{
			j = fibonacci(i) ;
			printf("Number=%d\n", j) ;
		}
		else
		{
			printf("It is NOt a correct input!\n") ;
		}

	}
	else
	{
		printf("It is NOt a correct input!\n") ;
	}
	return 0 ;
}
*/
