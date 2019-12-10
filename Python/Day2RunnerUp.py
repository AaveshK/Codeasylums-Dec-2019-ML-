#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    run=-101
    max=-101
    for i in arr:
        if i>max:
            run=max
            max=i
        elif i>run and i<max:
            run=i
    print(run)
'''
10/10 Test cases passed
Sample-Input_Output
3	Size
1 2 3	Data
2	Output
'''
