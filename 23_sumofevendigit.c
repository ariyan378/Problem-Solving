#include<stdio.h>

int main(){
     

    int n , sum = 0 , value = 0 ;
    printf("Enter your number : ");
    scanf("%d" , & n);

    while(n!=0){


        value = n % 10;
        n = n / 10 ;

        if(value%2==0){
     

        sum +=value ;
        }else{
           continue;
        }
    }

    printf("Your sum is %d",sum);

    return 0 ;

}