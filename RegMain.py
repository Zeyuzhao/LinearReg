import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from LinearRegClass import *
import time

time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
style.use('ggplot')

data = np.loadtxt('data.txt', delimiter=',',ndmin=2)

X = data[:, 0]
y = data[:, 1]

theta = np.array([10, 0])
l = LinearReg(X, y, 0.0240, initTheta=theta, iter = 1000)

l.gradientDescent()

t = l.theta



