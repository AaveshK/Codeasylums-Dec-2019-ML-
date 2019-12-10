#Q. From a given list, find the second smallest and second largest element
list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4] 
largest=list1[0]
smallest=list1[0]
sec_largest=list1[0]
sec_smallest=list1[0]
for item in list1[1:]:
    if item > largest:
      sec_largest=largest
      largest=item
    elif sec_largest<item:
      sec_largest=item
    if item<smallest:
      sec_smallest=smallest
      smallest=item
    elif sec_smallest>item:
      sec_smallest=item
print("Second smallest " + str(sec_smallest))
print("Second largest " + str(sec_largest))

'''Sample Input-Output
Second smallest 4                                                                                                              
Second largest 41
'''
