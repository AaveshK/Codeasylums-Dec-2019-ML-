'''Q. Write a Python program to count the number of strings where the string length is 2 or
more and the first and last character are same from a given list of strings.'''
ctr=0
words=[]
n = int(input())
for i in range(0, n):
    word = input()
    words.append(word)
for word in words:
	if len(word)>1 and word[0]==word[-1]:
		ctr=ctr+1
print(ctr)
'''
Sample-Input-Output
3
121
aba
abA
2
'''
