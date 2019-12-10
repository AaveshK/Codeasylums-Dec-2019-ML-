/*
Question: Input an array and rearrange the array such that jth index becomes i for all ith index values j
Arr[j]=i when Arr[i]=j
*/
#include<stdio.h>
void main()
{
    int i,j,size;
    int a[100];
    int b[100];
    scanf("%d",&size);
    for(i=0;i<size;i++)
        {
            scanf("%d",&a[i]);
        b[i]=a[i];
        }
    for(i=0;i<size;i++)
        {
            j=a[i];
            b[j]=a[i];
        }
    for(i=0;i<size;i++)
    printf("%d ",b[i]);
}
/*
Sample Input-Output
4
1 3 0 2
0 1 2 3
*/
