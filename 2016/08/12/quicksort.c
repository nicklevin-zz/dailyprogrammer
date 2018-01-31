#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <time.h>

//Takes in a list and length and returns if the list is sorted (1 yes, 0 no) 
void quicksort(long* list, long low, long high){
	long pivot, i, j, temp;
       		
	
	if(high > low){
		//pick a pivot
		pivot = list[high];
		//everything less than pivot goes left, more goes right
		for(i = low, j = low; j < high; j++){
			if(list[j] < pivot){
				temp = list[i];
				list[i] = list[j];
				list[j] = temp;
				i++;
			}
		}	
		temp = list[i];
		list[i] = list[high];
		list[high] = temp; 
	
		//call quicksort on remaining lists
		quicksort(list, low, i - 1);
		quicksort(list, i + 1, high);
	}
}

void generateRandomList(long* list, long length){ 
	long i;
	srand((unsigned) time(NULL)); 
	printf("RAND_MAX: %d\n", RAND_MAX);
	for(i = 0; i < length; i++)
		list[i] = (long) (rand() % RAND_MAX);  
}

int main(int argc, char** argv){
	long length, i, count;
	long* list;

	FILE *file;

	/*
	file = fopen("unsortedList.txt", "r");
	assert(file != NULL);
	
	fscanf(file, "%l", &length);
	assert(length > 0);
	*/
	length = 100000; 
	list = (long*) malloc(sizeof(long) * length);
	
	generateRandomList(list, length);
	/*read in all values into list array
	for(i = 0; i < length; i++)
		fscanf(file, "%l", list + i); 
	fclose(file);
	*/
	quicksort(list, 0, length - 1); 
	
	for(i = 0; i < length; i++){
		printf("%ld ", list[i]);
		count+=list[i];
	}
       	printf("\n Count: %ld\n", count);	

}
