#Q. Add two lists using map and lambda.
listA=[]
listB=[]
n=int(input())
for i in range(0,n):
    word=input()
    listA.append(word)
for i in range(0,n):
    word=input()
    listB.append(word)
C=list(map(lambda x, y: x+ ' ' +y, listA, listB))
print(*C, sep='\n')
'''
Sample-Input-Output
3
one
two
three
1
2
3
one 1
two 2
three 3
'''
