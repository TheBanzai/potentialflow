from flowlibrary import *
import matplotlib.pyplot as plt
import numpy as np

#define plot variables
x_start = -1
x_stop = 7
y_start = -4
y_stop = 4
N = 400     #steps
n_stream = 20
x_step = (x_stop-x_start)/(N*1.0) #multiplication by 1.0 to force float
y_step = (y_stop-y_start)/(N*1.0)

#define Flow
flow1 = SinkSource(20, 0, 0)
flow2 = translationFlowX(2)
flow3 = SinkSource(-20, -3, 0)

#define Matrix 1
Psi1 = makeMat(flow1, N, x_start, x_stop, y_start, y_stop)
Psi2 = makeMat(flow2, N, x_start, x_stop, y_start, y_stop)
Psi3 = makeMat(flow3, N, x_start, x_stop, y_start, y_stop)

Psi = Psi1+Psi2+Psi3

plotMat(Psi,N, n_stream , x_start, x_stop, y_start, y_stop)

