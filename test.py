import numpy as np

# b = np.zeros((1,40), dtype= int)
# c = np.random.randint(1,10, size =(1,41))
# d = np.hstack((b,c)).reshape(9,9)
# a = np.random.permutation(d.ravel()).reshape(9, 9)

b = np.arange(1,10)
c = np.vstack((b,b,b,b,b,b,b,b,b))
 

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
  
  b = np.array([0,0,0,0,0,0,0,0,9,])
  c = np.random.permutation(b.ravel()) 
  d = np.random.permutation(b.ravel()) 
  e = np.random.permutation(b.ravel()) 
  f = np.random.permutation(b.ravel()) 
  g = np.random.permutation(b.ravel()) 
  h = np.random.permutation(b.ravel()) 
  r = np.random.permutation(b.ravel()) 
  s = np.random.permutation(b.ravel()) 
  t = np.random.permutation(b.ravel()) 
  a = np.vstack((c,d,e,f,g,h,r,s,t))
  print(a)
  Exit = check_matrix(a)