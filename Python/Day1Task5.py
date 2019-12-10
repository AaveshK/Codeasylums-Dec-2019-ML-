#Q.Check if input number is palindrome or not
Number1 = int(input("Please Enter any Number: "))  
Number1n=Number1  
Reverse1 = 0    
while(Number1 > 0):    
    Reminder1 = Number1 %10    
    Reverse1 = (Reverse1 *10) + Reminder1    
    Number1 = Number1 //10
if (Number1n==Reverse1):
  print("\n Palindrome")
else:
  print("Not palindrome")

'''Sample Input-Output
Please Enter any Number: 123                                                                                                   
Not palindrome

Please Enter any Number: 12321                                                                                                 
                                                                                                                               
Palindrome
'''
