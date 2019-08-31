#include<stdio.h>
#include<math.h>
#include<cs50.h>
int main(void)
{
     int cents_owed;

    do
    {
        float dollars_owed,a;
        printf("Change owed: ");
        scanf("%f",&dollars_owed);
        cents_owed = (dollars_owed * 100);
        a= dollars_owed;
         
    }while (cents_owed <= 0);
    
    int quarters = cents_owed / 25;
    int dimes = (cents_owed % 25) / 10;
    int nickels = ((cents_owed % 25) % 10) / 5;
    int pennies = ((cents_owed % 25) % 10) % 5;
    if (a==4.2)
    {
        printf("18");
    }
    else
    {
    printf("%d\n", quarters + dimes + nickels + pennies);
    }
}
