'''
Q. Input the seat number and classify in into Window,Middle,Aisle seat and also find the similar seat in next row
W M A   W M A
1 2 3   4 5 6
7 8 9  10 11 12
W M A   W M A
'''
lim=100
seat1=input("Enter seat 1 :")
seat2=input("Enter seat 2 :")
if(int(seat1)%6==0 or ((int(seat1)+5)%6==0)):
  print("Window seat")
elif(int(seat1)+4%6==0 or ((int(seat1)+1)%6==0)):
  print("Middle seat")
else:
  print("Aisle seat")
print("Seat in next row is " + str(int(seat1)+6))

if(int(seat2)%6==0 or ((int(seat2)-1)%6==0)):
  print("Window seat")
elif(int(seat2)-2%6==0 or ((int(seat2)+1)%6==0)):
  print("Middle seat")
else:
  print("Aisle seat")
print("Seat in next row is " + str(int(seat2)+6))

''' Sample Input-Output
Enter seat 1 :3
Enter seat 2 :3
Aisle seat
Seat in next row is 9
Aisle seat
Seat in next row is 9
'''
