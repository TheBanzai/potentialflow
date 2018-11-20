# potentialflow
Visualize potential flow

Florian Gschwandtner
Version 0.1

flowlibrary.py is the main part of this program. There are some basic flow functions and some functions for visualisation defined within it.

At the moment there is no way to use this but to modify matrixVisualize.py or visualizeFlow.py directly.

For the SinkSource Distribution a equation in the form:
Q(x')=q/p*(-1/3*x'³+2*x'²-(2+p)*x'+p) is implemented, where Q(x') is the source strength in a normalized Interval [0,1] p is the point of maximum thickness in a range of [0,1] and q is Q(x'=0).
