from numpy.random import rand
import matplotlib
from matplotlib.pyplot import savefig
import matplotlib.pyplot as plt
import numpy as np
from numpy import *


def draw_pic(x,pic_name):
    lens = len(x)
    y = np.asarray(sort(x))
    x = np.arange(1,lens+1,1)
    plt.scatter(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(pic_name)
    plt.savefig(pic_name+'.png')


