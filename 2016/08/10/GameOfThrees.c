#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

int main(int argc, char** argv){
	int number = 0;
	
	assert(argc == 2);

	number = atoi(argv[1]);
	
	assert(number > 0);
	
	while(number != 1){
		switch(number % 3){
			case 0:
				printf("%d 0\n", number);
				number = number / 3;
				break;
			case 1: 
				printf("%d -1\n", number);
				number = (number - 1) / 3;
				break;
			case 2: 
				printf("%d 1\n", number);
				number = (number + 1) / 3;
				break;
		}
	}
	printf("1\n");
}

