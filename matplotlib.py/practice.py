import matplotlib.pyplot as plt
import numpy as np
#plot 1:
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(x,y)

#plot 2:
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(1,2,2)
plt.plot(x,y)
fontone ={
"text" : "family of font one",
"fontfamily" : "sans-serif",
"font" : "Arial",
"fontstyle" : "italic",
"color" : "darkred",
"size" : 20}
saved = fontone.get("text")
saved_conv = str(saved)
#saved_conv = saved_conv.upper()
#fontone.update({"text" : saved_conv})
plt.plot(x,y,)

# print(saved_conv, isinstance(saved_conv, str))
# print(saved_conv)
#plt.title( saved_conv, fontdict=fontone, loc="right")
#plt.grid()
#plt.grid(axis="both", ls= "--",lw=3.5,c ="r")
plt.show()