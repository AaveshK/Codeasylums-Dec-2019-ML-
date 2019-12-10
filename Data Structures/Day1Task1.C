/*
Q. Input an array and rotate elements left, k times
*/
#include<stdio.h>
void main()
{
    int i,j,size,k,temp;
    int a[100];
    scanf("%d",&size);
    for(i=0;i<size;i++)
        scanf("%d",&a[i]);
    scanf("%d",&k);
    while(k>0)
    {temp=a[0];
        for(i=0;i<size-1;i++)
          a[i]=a[i+1];
        a[size-1]=temp;
        k--;
    }
    for(i=0;i<size;i++)
        printf("%d ",a[i]);
}
/*
Sample Input-Output
6
3 6 7 8 9 3
2
7 8 9 3 3 6
*/
