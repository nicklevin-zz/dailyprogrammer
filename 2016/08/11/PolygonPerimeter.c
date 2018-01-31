#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#include <assert.h>


double ComputePolygonPerimeter(int numSides, double circumradius){
	return numSides *  circumradius * 2 * sin(M_PI / numSides); 
}


int main(int argc, char** argv){
	double circumradius;
	int numSides; 
	
	assert(argc == 3);
	
	sscanf(argv[1], "%d", &numSides);
	sscanf(argv[2], "%lf", &circumradius);

	printf("%lf\n", ComputePolygonPerimeter(numSides, circumradius));
}

