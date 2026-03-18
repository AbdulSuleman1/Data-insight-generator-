# c = "081"
# w = c + "38" 
# print(("my string is:"), w)
# print(("my float is :"),float(w) + 10)
# c =  "0812"
# print(float(c))

# import numpy as np
# x = np.array([2,4,])
#import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,6])
y = np.array([0,250])
plt.plot(x,y, marker = "H",ms = '15', mec ='r', mfc = 'y')
plt.show()

x1 = np.array([1,2,6,8])
y1 = np.array([3,8,1,10])
plt.plot(x1,y1,'*-r')
plt.show()


#print(mp.__version__)
