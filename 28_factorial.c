#include<stdio.h>

int main(){
     

    int n , product = 1;
    printf("Enter your number : ");
    scanf("%d" , & n);

    for( int i = 1  ; i <= n ; i++){
        product = product*i;
    }
   printf(" the factorial is %d", product);



  return 0 ;
}  