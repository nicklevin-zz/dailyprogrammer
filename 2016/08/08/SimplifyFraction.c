
#include <stdio.h>
#include <stdlib.h>


int main(int argc, char** argv){

	int numerator, denominator;
	int divisor = 2;
	int flip = 0;
	
	if(argc != 3 ){
		printf("Wrong number of params!\n");
		exit(0);
	}
		
	numerator = atoi(argv[1]);
	denominator = atoi(argv[2]);
	if(numerator < 1 || denominator < 1)
	{
		exit(0);
	}
	
	if(numerator == 1 || denominator == 1){
		;	//do nothing, fraction is simplified already
	}

	else{
		if(numerator > denominator){
			flip = numerator;
			numerator = denominator;
			denominator = flip;
		}
		if((denominator % numerator) == 0){  //means it divides perfectly
			denominator = denominator / numerator; 
			numerator = 1; 
		}
		else{
			while(divisor < numerator)
			{
				if(numerator % divisor == 0 && denominator % divisor == 0){
					numerator = numerator / divisor;
					denominator = denominator / divisor;
					divisor = 2; 
				}
				else{
					divisor++;
				}
			}
		}
	}
	if(flip != 0){
		flip = numerator;
		numerator = denominator;
		denominator = flip;
	}
	printf("%d %d\n", numerator, denominator);		
}

