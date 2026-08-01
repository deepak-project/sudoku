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
            # print("You enter the worng number")
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
            # print("You enter the worng number")
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
                #    print("You enter the worng number")
                   return 0
    
    return 1       



a = np.zeros((9,9))
# b = 0
# while b == 0:
#     x = np.random.randint(1, 10)
#     a[0,0] = x
#     a[0,1] = 1
#     b = check_matrix(a)
# print(a)
# print(b)


for i in range(9):
   
  for j in range(9):
    b = 0
    while b == 0:
      x = np.random.randint(1,10)
      a[i,j] = x
      b = check_matrix(a)
     
    print(a)
     

print(a)
      