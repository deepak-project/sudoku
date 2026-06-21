import numpy as np

b = np.arange(1,10)
# print(b)

# c = np.vstack((b,b,b,b,b,b,b,b,b))
# print(c)

a = np.random.permutation(b.ravel()) 

b = np.random.permutation(b.ravel()) 
c = np.vstack((b,a))
print(c)
