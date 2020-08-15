import numpy as np, matplotlib.pyplot as plt
#I hold x a line while defining new values for each y
x = np.linspace(0, 20, 2000)
#1*x[1] + 0*x[2] <= 5
#y0*0=5-x  #No initialization with respect to y0 because it is zero.
#0*x[1] + 1*x[2] <= 5
y1=5+x*0
#1*x[1] + 0*x[2] >= 1
#y2*0=1-x  #No inititialization
#0*x[1] + 1*x[2] >= 1
y3=1-x*0
#1*x[1] + 1*x[2] <= 6
y4=6-x

plt.plot(x,y4,label=r'$x[1]+x[2]<=6$')
plt.plot(x,y1)
plt.axvline(5, color='g')        #y2 <  5
plt.axvline(1, color='r') #x  >= 1
plt.plot(x,y3,'b--')  #y3 >= 1

plt.fill_between(x, y1, y4, where=(x>1)&(x<5), color='grey', alpha=0.5)
plt.show()