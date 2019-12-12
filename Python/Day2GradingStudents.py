#Grading Students: Accepted on HackerRank
n=int(input())
lst=[]
for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele)

for i in range(0,n):
    if lst[i]<38:
        print(lst[i], sep = "\n")
    elif (lst[i]%5)>=3:
        lst[i]=lst[i]+5-(lst[i]%5)
        print(lst[i],sep="\n")
    else:
        print(lst[i],sep="\n")
'''
Sample-Input-Output
4
73
67
38
33

75
67
40
33
'''
