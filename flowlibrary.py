#Florian Gschwandtner
    
#Version 0.1

#library for basic potential flow functions returning an y value given
#a constant and an x value

from math import atan2, sin, cos, tan, log, sqrt, pi, e
from numpy import zeros
import matplotlib.pyplot as plt

class Flow:
    #For later ease of modification
    def __init__(self):
        pass

class translationFlowX(Flow):
    def __init__(self, u_inf):
        self.u = u_inf
    
    #returning a y value given const. and x
    def value(self, c, x):
        return c/self.u

    def psi(self, x, y):
        return self.u*y

class translationFlowY(translationFlowX):
    #doesn't work, needs fixing
    def value(self, c, x):
        return -self.u*x        

    def psi(self, x, y):
        return -self.u*x

class stagnationFlow(Flow):
    #stagnation Point Flow: a positive
    def __init__(self, a):
        self.a = a
    
    #Warning! carefull which quadrant
    def value(self, c, x):
        return c/(self.a*x)

    def psi(self, x, y):
        return self.a*x*y

class SinkSource(Flow):
    #Q positive for source, negative for sink
    def __init__(self, Q, x0, y0):
        self.Q = Q
        self.x0 = x0
        self.y0 = y0

    def value(self, c, x):
        return (x-self.x0)*tan((2*pi*c)/self.Q)+self.y0

    def psi(self, x, y):
         return self.Q/(2*pi)*atan2(y+self.y0,x+self.x0)

class Vortex(Flow):
    def __init__(self, gamma):
        self.gamma = gamma
 
    def value(self, c, x):
        return sqrt(e**(-(4*pi*c)/self.gamma)-x**2)
    
    def psi(self, x, y):
        self.r = sqrt(x**2+y**2)
        if self.r != 0:
            return -(self.gamma/(2*pi))*log(self.r)
        else:
            return 0

def makeMat(func, N, x_start, x_stop, y_start, y_stop):
    #carefull: first matrix argument is y value!
    x_step = (x_stop-x_start)/(N*1.0) #multiplication by 1.0 to force float
    y_step = (y_stop-y_start)/(N*1.0)
    Mat = zeros((N,N))
    for k in range(0,N):
        y = y_stop-k*y_step
        for l in range(0,N):
            x = x_start+l*x_step
            Mat[k][l] = func.psi(x,y)
    return Mat

def plotMat(Mat, N, n_stream, x_start, x_stop, y_start, y_stop):
    #find min and max constant in matrix
    mi = Mat[0][0]
    ma = mi
    matlen = range(0,N)    
    for k in matlen:
        for l in matlen:
            if Mat[k][l]>ma:
                ma = Mat[k][l]
            elif Mat[k][l]<mi:
                mi = Mat[k][l]
            else:
                pass

    YES = zeros((N,N))
    streamVal = []
    constlen = (ma-mi)/n_stream
    for i in range(0,n_stream):
        streamVal.append(mi+i*constlen)

    #needed for visualization purposes
    streamVal.append(ma+1)

    for k in matlen:
        for l in matlen:
            for c in range(0,n_stream):
                if (streamVal[c]<=abs(Mat[k][l])<=streamVal[c+1]):
                    YES[k][l] = c
                else:
                    YES[k][l] = YES[k][l]

    x_step = (x_stop-x_start)/(N*1.0) #multiplication by 1.0 to force float
    y_step = (y_stop-y_start)/(N*1.0)
    x_vec = zeros(N)
    y_vec = zeros(N)
    for i in range(0,N):
        x_vec[i] = x_start+i*x_step
        y_vec[i] = y_start+i*y_step
    
    for k in matlen:
        for l in matlen:
            if 1:
                pass
                #plt.plot(x_vec[k],y_vec[k], marker='.', color='b')
            else:
                pass
    plt.matshow(YES)
    plt.show()
