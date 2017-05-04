from numpy.random import rand
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy import *

x = rand(10, 1)
# basic
plt.scatter(x[:, 0])
plt.xlabel('x')
plt.ylabel('y')
plt.title('test')
plt.show()