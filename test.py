import numpy as np

b = np.zeros((1,40), dtype= int)


c = np.random.randint(1,10, size =(1,41))


d = np.hstack((b,c)).reshape(9,9)
 


 
a = np.random.permutation(d.ravel()).reshape(9, 9)

print(a)