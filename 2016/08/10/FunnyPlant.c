
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main(int argc, char** argv){
	double people = 0, plants = 0, fruits = 0;
	int weeks = 1;
	clock_t start, end;

	printf("Enter number of people:\n");
	scanf("%lf", &people);
	printf("Enter number of starting fruits:\n");
	scanf("%lf", &plants);

	start = clock();
	while(fruits < people){
		fruits += plants; 
		plants += fruits;
		weeks++;		
	}
	end = clock();
	printf("\n%d\n",(int) weeks);
	printf("%f seconds\n", (double) (end - start)/CLOCKS_PER_SEC);
}
