from flowlibrary import *
import matplotlib.pyplot as plt
import numpy as np

#define plot variables
x_start = -3
x_stop = 3
y_start = -3
y_stop = 3
N = 200     #steps
n_stream = 20
x_step = (x_stop-x_start)/(N*1.0) #multiplication by 1.0 to force float
y_step = (y_stop-y_start)/(N*1.0)

#define Flow
flow1 = translationFlowX(2)
flow2 = Vortex(10)
flow3 = SinkSource(-10, 0, 0)


#define Matrix
Psi1 = makeMat(flow1, N, x_start, x_stop, y_start, y_stop)
Psi2 = makeMat(flow2, N, x_start, x_stop, y_start, y_stop)
Psi3 = makeMat(flow3, N, x_start, x_stop, y_start, y_stop)

#Because of the linearity property of potential flow you can simply add the Matrix elements to get a combined flow
Psi = Psi1+Psi2

plotMat(Psi,N, n_stream , x_start, x_stop, y_start, y_stop)

