#include <stdio.h>
 
int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
      int n;
     int dig, revNumber;

    scanf("%d",&n);
 
    /*Reversing Number*/
    revNumber=0;
    
    while(n>0)
    {
        dig=n%10; /*get digit*/
        revNumber=(revNumber*10)+dig;
        n=n/10;
    }
    
    printf("%d\n",revNumber);
      
    }
}
    


