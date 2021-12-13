import random
import matplotlib.pyplot as plot
import numpy as np
import time

def fractal(x1,y1,t,d):
    if d < 1:
        return

    x2 = x1 + np.cos(t)*d
    y2 = y1 + np.sin(t)*d


    if d > 0:
        plot.plot([x1, x2], [y1, y2])

        fractal(x2, y2, t + np.pi/9, d-1)
        fractal(x2, y2, t - np.pi/9, d-1)



fractal(0, 0, np.pi/2, 11)
plot.show()