#include <stdio.h>
#include <stdlib.h>
test
void out(void){
	printf("atexit() succeeded!\n");
}

int main(void){
	if(atexit(out))
		fprintf(stderr,"atrxit() failed!\n");
	return 0;
}
