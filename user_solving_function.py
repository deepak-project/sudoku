zero = np.sum(a == 0) 
 
while zero != 0:
  print(a)
  z = int(input('Enter your number: '))
  i = int(input("Enter your row number: "))
  j = int(input('Enter your column number: '))
  a[i-1,j-1] = z
  b = check_matrix(a)

  if b == 1:
    zero = zero - 1
  else:
    a[i-1,j-1] = 0

    
print("Congralustion! You Sloved The Game")