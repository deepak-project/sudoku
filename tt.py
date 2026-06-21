import numpy as np

b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
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
a = np.vstack(row_list)
print(a)
