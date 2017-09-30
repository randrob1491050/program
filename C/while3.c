#include <stdio.h>

int no9(int n)
{
	int sum=0;
	int i=1;
	while(i<=n)
	{
		if(i%10==9) sum++; 
		if(i/10%10==9) sum++;
		++i;
	}
	return sum;
}

int main(void)
{
	printf("no9(100) = %d\n", no9(100));
	printf("no9(80) = %d\n", no9(80));
	
	return 0;
}

/*
#include <stdio.h>

int count(int n){
        int c = 0; // 9's count
        int a;// 个位数字
        int n_tmp = n;
        while(n > 0){
                a = n % 10;
                if(a == 9) c++;
                n = n / 10;

        }
        printf("%d   %d\n", n_tmp, c);
        return c;
}

int main(void){
        int num = 0;
        int i;
        for(i = 1; i <= 100; i++){
                num += count(i);
        }
        printf("total 9: %d\n", num);
}
*/
