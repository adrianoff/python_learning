import numpy as np

x = 5.0
y = 7.0
lmb = 0.1

w1 = 1.0
w2 = -1.0
w3 = 2.0

u = np.tanh(w1*x)
z = np.tanh(w2*u)
yhat = w3*z

dL_yhat = 2 * (yhat - y)
dL_w3 = 2 * (yhat - y) * z

w3 = w3 - lmb * dL_w3


