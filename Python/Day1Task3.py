#Q. Input a number and reverse it
Number = int(input("Please Enter any Number: "))    
Reverse = 0    
while(Number > 0):    
    Reminder = Number %10    
    Reverse = (Reverse *10) + Reminder    
    Number = Number //10    
     
print("\n Reverse of entered number is = %d" %Reverse)
'''
Please Enter any Number: 321

Reverse of entered number is = 123
'''
