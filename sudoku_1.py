import numpy as np

def check_matrix(a):
    for i in range(9):
      for j in range(9):
        for k in range(9):
           n = a[i,j]
           m = a[i,k]

           if n != m:
            pass

           elif j == k:
            pass
           
           elif (a[i,j] == 0) and (a[i,k] == 0):
             pass

           else:
             
            return 0
           
    for i in range(9):
      for j in range(9):
        for k in range(9):
           n = a[j,i]
           m = a[k,i]

           if n != m:
            pass

           elif j == k:
            pass
           
           elif (a[j,i] == 0) and (a[k,i] == 0):
             pass

           else:
              
            return 0
           
    for p in [0,3,6]:
      for q in [0,3,6]:
        for i in range(p,3 + p):
          for j in range(q,3 + q):
            for k in range (p,3 + p):
              for l in range (q,3 + q):
                n = a[i,j]
                m = a[k,l]

                if n != m:
                  pass

                elif (i == k) and (j == l):
                  pass

                elif (a[i,j] == 0) and (a[k,l] == 0):
                  pass

                else:
                    
                   return 0
    
    return 1        




Exit = 0
while Exit == 0:
  s = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
  b = np.random.permutation(s.ravel()) 
  c = np.roll(b, -1)
  d = np.roll(b, -2)
  e = np.roll(b, -3)
  f = np.roll(b, -4)
  g = np.roll(b, -5)
  h = np.roll(b, -6)
  r = np.roll(b, -7)
  s = np.roll(b, -8)
  t = np.roll(b, -9)
  row_list = [c, d, e, f, g, h, r, s, t]
  np.random.shuffle(row_list)
  base = np.vstack(row_list)
  Exit = check_matrix(base)
 


num_zeros = int(input("Enter you many vacant position in sudoku you want: "))

def generate_sudoku(num_zeros):

    sudoku = base.copy()
 
    perm = np.random.permutation(9) + 1
    for i in range(9):
        sudoku[sudoku == i + 1] = -perm[i]
    sudoku = -sudoku

    idx = np.random.choice(81, num_zeros, replace=False)
    sudoku.flat[idx] = 0

    return sudoku

a = generate_sudoku(num_zeros)




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
    print("You enter the worng number! Try again")

    
print("Congralustion! You Sloved The Game")
     

