#ADDREV on SPOJ (accepted)
def rever(a):
    rev=0
    while(a>0):
        dig=a%10
        rev=rev*10+dig
        a=a//10
    return(rev)
n=int(input())
for i in range(n):
    x, y = [int(x) for x in input().split()]  
    print(rever(rever(x)+rever(y)))
''' 
Sample Input-Output

3
24 1
4358 754
305 794

34
1998
1
'''
