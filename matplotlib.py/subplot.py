import matplotlib.pyplot as plt
import numpy as np
f ="how subplot looks like"
plt.title(f.upper(),loc="center")
#plot1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(3,3,1)
plt.plot(x,y,"+-r", lw=5,ms=14)

#plot2
x8 = np.array([0,1,2,3])
y8 = np.array([10,20,30,40])
plt.subplot(3,3,2)
plt.plot(x,y,"+-r", lw=5,ms=14)

#plot3
x7 = np.array([0,1,2,3])
y7 = np.array([3,8,1,10])
plt.subplot(3,3,3)
plt.plot(x,y,"+-r", lw=5,ms=14)

# #plot4
x6 = np.array([0,1,2,3])
y6 = np.array([3,8,1,9])
plt.subplot(3,3,4)
plt.plot(x,y,"+-r", lw=5,ms=14)

# #plot5
x5 = np.array([0,1,2,3])
y5 = np.array([3,8,1,4])
plt.subplot(3,3,5)
plt.plot(x,y,"+-r", lw=5,ms=14)

# plot6
x3 = np.array([0,1,2,3])
y3 = np.array([3,8,1,9])
plt.subplot(3,3,6)
plt.plot(x,y,"+-r", lw=5,ms=14)

# #plot7
# x2 = np.array([0,1,2,3])
# y2 = np.array([3,8,1,5])
# plt.subplot(3,2,7)
# plt.plot(x,y,"+-r", lw=5,ms=14)

# #plot8 
# x1 = np.array([0,1,2,3,6])
# y1 = np.array([3,8,1,9])
# plt.subplot(3,2,8)
# plt.plot(x,y,"+-r", lw=5,ms=14)



plt.show()

