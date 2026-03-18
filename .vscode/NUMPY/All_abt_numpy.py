import numpy as np
arrn= np.array([1,2,3,4,5])
print(arrn)
print(np.__version__)
arr = np.array([74])# 0-D array or scalar
arrr = np.array([2,3,4]) # 1 - D array
arrrr = np.array([[2,3,4,5],[2, 6, 7,5]]) # 2 -D(array must be equal)
print(arrrr)
arrrrr = np.array([[[[2,3,4],[1,4,5]],[[9,7,9],[9,6,5]]]])
print(arrrrr)

#ndim => tell us how many dimension the array has
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[[1,2,3],[4,5,6]],[[7,8,9],[9,6,3]]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
# higer dim array

aer = np.array([1,2,3,4], ndmin= 5)
print(aer)
print("number of dim:", aer.ndim)