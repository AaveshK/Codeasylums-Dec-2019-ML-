#Input a number and print Hello n times for every digit in new line, where n is the digit starting from left
n=input("Enter number")
num_str = str(n)
for num in num_str:
  for x in range(int(num)):
    print("Hello" + str(x+1) + " ",end=" ")
  print("\n")
'''Sample Input-Output
Enter number 431
Hello1  Hello2  Hello3  Hello4

Hello1  Hello2  Hello3

Hello1
'''
