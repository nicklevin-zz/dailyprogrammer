#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <stdbool.h>

int compare_ints (const void *a, const void *b)
{
	const int* val1 = (const int*) a;
	const int* val2 = (const int*) b;

	return (*val1 > *val2) - (*val1 < *val2);
}

int main(int argc, char** argv){
	FILE *fp;
	int* intervals;
	char line_buff[256]; 	
	int i, num_switches, low, high;
	clock_t start, end; 	
	int num_intervals = 0, count = 0;

	if(argc != 2){
		printf("Wrong number of inputs! Usage: *.out [input file]\n");
		exit(0);
	}

	start = clock();
	
	fp = fopen(argv[1], "r");
	if(fp == NULL){
		printf("File not found!\n");
		exit(0);
	}

	fscanf(fp, "%d", &num_switches);
	fgets(line_buff, 256, fp); // read to end of first line	
	while(fgets(line_buff, 256, fp) != NULL){	//count remaining lines to get number of intervals
		num_intervals++;
	}
	
	printf("Number of intervals: %d\n", num_intervals);

	rewind(fp);

	fscanf(fp, "%d", &i); //read first line and throwaway

	intervals = (int*) malloc(sizeof(int) * num_intervals  * 2);
	
	for(i = 0; i < num_intervals * 2; i += 2)
	{
		fscanf(fp, "%d %d", &low, &high);
		if(low > high){
			intervals[i] = high;
			intervals[i+1] = low+1;
		}
		else{
			intervals[i] = low;
			intervals[i+1] = high+1; 
		}
		//printf("Low: %d --- High: %d\n", low, high); 
	}

	fclose(fp);	
	
	qsort(intervals, num_intervals * 2, sizeof(int), compare_ints);	

	for(i = 0; i < num_intervals * 2; i+=2){
		count += intervals[i+1] - intervals[i];
	}
	
	end = clock();
	
	free(intervals);
	printf("Final Count: %d\nTime: %f seconds\n", count, (double)(end - start) / CLOCKS_PER_SEC);
}

