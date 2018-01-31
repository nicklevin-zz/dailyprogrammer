#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>
#include <assert.h>
#include <string.h>

//returns array of decimal values indicating how many of 
// each number from 1 to NUM_SIDES was rolled (0 to 1 scale) 
void rollDice(float* results, long numRolls, int numSides){
	long i, number;
	long rollCount[numSides];
	
	for(i = 0; i < numSides; i++)
	{	
		rollCount[i] = 0;
	}

	srand(time(NULL)); //seed random number generator
	
	for(i = 0; i < numRolls; i++){
		number = rand() % numSides;
		rollCount[number]++;
		//printf("Roll #%ld is a %ld\n", i+1, number + 1); 
	}
	//printf("COUNT: \t\t");
	for(i = 0; i < numSides; i++){
		results[i] = (float) rollCount[i] / numRolls;
		//printf("%ld: %ld\t", i + 1, rollCount[i]);
	}
	//printf("\n");
}

int main(int argc, char** argv){
	long i, numRolls;
	int numSides;
	float* results; 
	char* buff;

	assert(argc == 3);

	numRolls = strtol(argv[1], &buff, 10);
       	numSides = atoi(argv[2]);	
	
	printf("%ld rolls ... \t", numRolls);
	if(numRolls < 10000) printf("\t");

	results = (float*) malloc(sizeof(float) * numSides);

	rollDice(results, numRolls, numSides); 	
	for(i = 0; i < numSides; i++){
		printf("%ld: %.3f\t", i + 1, results[i]);
	}
	printf("\n");

}
