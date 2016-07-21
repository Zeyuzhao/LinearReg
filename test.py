import pylab as plt
import numpy as np

plt.subplot(211)
x = [1,10]
y = [30, 1000]
plt.loglog(x, y, basex=10, basey=10, ls="-")



plt.subplot(212)
x = [10,100]
y = [10, 10000]
plt.loglog(x, y, basex=10, basey=10, ls="-")

plt.show()