#include <stdio.h>
#include <stdlib.h>

void isPrime(int number) {
    printf("test");
 int flag = 0;
 if (number < 2)
  flag = -1;
 else {
  for (int i = 2; i <= number / 2; i++) {
   if (number % i == 0) {
    flag = 1;
    break;
    }
 }
 }

 switch (flag) {
  case -1:
   printf("Undefined");
   break;
  case 0:
   printf("The number is prime");
   break;
  case 1:
   printf("The number is not prime");
   break;
  default: printf("Error");
}
}

int main(){
    isPrime(45);
}