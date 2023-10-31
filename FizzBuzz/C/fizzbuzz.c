// A Simple fizzbuzz implemetation written using the C programming language

#include <stdio.h>

void fizzbuzz(int limit, int fizz, int buzz) {
    int i;
    for (i = 1; i <= limit; i++) {
        if (i % fizz == 0 || i % buzz == 0) {
              if (i % fizz == 0) {
                 printf("Fizz");
	        } if (i % buzz == 0) {
                 printf("Buzz");
	    }
	}
	else {
            printf("%d", i);
	}
	printf("\n");
    }
}

int main() {
    fizzbuzz(100, 3, 5);
    return 0;
}
