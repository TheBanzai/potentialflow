from flowlibrary import *
import matplotlib.pyplot as plt
import numpy as np

#plot variables
x_start = -10
x_stop = 10
y_start = -10
y_stop = 10
N = 400         #steps

#flow field
f = translationFlowX(1)
g = SinkSource(3, 2, 0)

#const in corner needs work
c1 = f.psi(x_start, y_start)+g.psi(x_start, y_start)
c2 = f.psi(x_stop, y_stop)+g.psi(x_stop, y_stop)
c1 = -abs(int(round(c1)))
c2 = abs(int(round(c2)))
const = [i for i in range(-20, 20, 1)]


x = np.linspace(x_start, x_stop, N)

for c in const:
    y=np.zeros(len(x))
    for k in range(0, len(x)):
        y[k] = f.value(c, x[k])+g.value(c, x[k])
    plt.plot(x,y)

plt.axis([x_start, x_stop, y_start, y_stop])
plt.grid()
plt.show()

