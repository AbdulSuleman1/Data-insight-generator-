import matplotlib.pyplot as plt
import numpy as np 

# data1 = np.array([10,500])
# data2 = np.array([20,600])
# plt.plot(data1,data2)
x1 = np.array([1,8, 20, 30])
y2 = np.array([3,10, 15, 25])
#plt.plot(x1, y2,"o") to eraze the line 0n ur graph
#plt.plot(x1, y2, "*", c ='green') the * tells us what sign to use 
plt.plot(x1, y2, marker= "*", c ='green')
plt.show()

y3 = np.array([2,10,20,30])
plt.plot(y3,'o--y', ms = 20, mec='k', mfc='g')
plt.show()

# print(plt.__version__) # to check your version



