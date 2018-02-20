//Problem proposed at: https://practice.geeksforgeeks.org/problems/find-the-most-frequent-digit/0

/*Initially started with by using a 'long long' for inputs, but changed
 to using string and scanning char-by-char to handle extra long (100 digit+) inputs
*/
#include <stdio.h>
#include <stdlib.h>

int main() {
	int input_count, i, j, max_digit, max_digit_amount;
	char** inputs; //array of strings for storing inputs
  int digitCount[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	scanf("%d", &input_count);
	inputs = malloc(input_count * sizeof(char*));  //space for input pointers
	for(i = 0; i < input_count; i++){
    inputs[i] = malloc(1000); //max input is 1000 digits
	    scanf("%s", inputs[i]);
	}
  for(i = 0; i < input_count; i++){
    //go through each digit in string until hitting null termination
    for(j = 0; inputs[i][j] != '\0'; j++){
      digitCount[inputs[i][j] - '0']++;   //subtract ASCII '0' to get digit value
    }
    //find most used digit
    max_digit = 0;
    max_digit_amount = digitCount[0];
    for(j = 0; j < 10; j++){
      if(digitCount[j] >= max_digit_amount){
        max_digit = j;
        max_digit_amount = digitCount[j];
      }
      digitCount[j] = 0;  //reset counts for next run
    }
    printf("%d\n", max_digit);
  }
	return 0;
}
