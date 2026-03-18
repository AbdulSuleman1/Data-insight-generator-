import matplotlib.pyplot as plt
import numpy as np

items = np.array(["indomie","garri","beans","rice"])
prices =np.array([7500,31000,65000,80000])
plt.subplot(3,3,1)
plt.bar(items,prices,color="r")


#for linegraph
x = np.array([0,1,2,3])
y = np.array([80000,65000,31000,7500])
plt.subplot(3,3,2)
plt.plot(x,y,"o:k")

#for scatter plot
items = np.array([0,1,2,3])
price = np.array([80000,65000,31000,7500])
plt.subplot(3,3,3)
plt.scatter(items,price)

# #for histogram
prices1 =np.array([80000,65000,31000,7500])
plt.subplot(3,3,4)
plt.hist(prices1)

plt.tight_layout()
plt.show()
