#Linear Search
def search(arr, x): 
  
    for i in range(len(arr)): 
  
        if arr[i] == x:
            return(i+1)
    return -1
arr=[]
r=int(input())
for i in range(0, r): 
    ele = int(input())
    arr.append(ele)
x=int(input())
if(search(arr,x)==-1):
    print("Not found")
else:
    print("Found at "+str(search(arr,x)))
'''
4 Size
1 Data
2
3
4 
3 Search Element                                                                                                                             
Found at 3
'''
