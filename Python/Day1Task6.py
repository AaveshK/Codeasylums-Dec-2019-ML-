#Q. Print a pettern
for i in range(5):
  for j in range(5):
    if j>=i:
      print(j+1,end=" ")
    else:
      print(" ", end=" ")
  print("\n", end='')
  
  '''Output for n=5
  1 2 3 4 5 
    2 3 4 5 
      3 4 5 
        4 5 
          5 
  '''
