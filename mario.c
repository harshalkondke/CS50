#include <cs50.h>
#include <stdio.h>
void mario()
{
    int n,j,k,i;
    do{
        printf("Height: ");
        scanf("%d", &n);
    }while(n<1 || n>8);
    for (i=1; i<=n; i++)
    {
        //print spaces
        for (j=n; j>i; j--)
        {
            printf(" ");
        }
        //print #
        for (k=1; k<=i; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}
int main(void)
{
    //main will call function mario
    if (true){
        mario();
    }
}
