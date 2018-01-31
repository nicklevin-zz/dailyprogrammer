#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <time.h>

int main(int argc, char** argv){
	unsigned int i, numTries, tactic1Count = 0, tactic2Count = 0;
        unsigned int prizeDoor, guessDoor1, guessDoor2;
	float tactic1, tactic2;
	assert(argc == 2);
	
	numTries = atoi(argv[1]);

	assert(numTries > 0);
	
	srand(time(NULL));

	for(i = 0; i < numTries; i++){
		prizeDoor = rand() % 3; 
		guessDoor2 = guessDoor1 = rand() % 3;
		guessDoor2 = (((guessDoor2 - 1) % 3) == prizeDoor) ? (guessDoor2 - 1) % 3 : (guessDoor2 + 1) % 3;  
		tactic1Count = (guessDoor1 != prizeDoor) ? tactic1Count : tactic1Count + 1; 
		tactic2Count = (guessDoor2 != prizeDoor) ? tactic2Count : tactic2Count + 1; 	
	}

	tactic1 = (float) tactic1Count / numTries;
	tactic2 = (float) tactic2Count / numTries;

	printf("----------\n%d prizes awarded!\n\tTactic 1: %.2f%% winning chance\n\tTactic 2: %.2f%% winning chance\n", numTries, tactic1 * 100, tactic2 * 100);
}
