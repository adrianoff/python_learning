import numpy as np



def th(arg):
    return np.tanh(arg)


def dth(arg):
    return 1 - np.tanh(arg) ** 2


x = 5
y = 7

w1 = 1.0
w2 = -1.0
w3 = 2.0

lmb =0.1

u = th(w1 * x)
z = th(w2 * u)
yhat = w3 * z

dL_yhat = 2 * (yhat - y)
dL_w3 = 2 * (yhat - y) * z
new_w3 = w3 - lmb*dL_w3
print(dL_w3, new_w3)


dL_w2 = dL_yhat * w3 * dth(u*w2) * u
new_w2 = w2 - lmb*dL_w2
print(dL_w2, new_w2)

dL_w1 = dL_yhat * w3 * dth(u*w2) * w2 * dth(x*w1) * x
new_w1 = w1 - lmb*dL_w1
print(dL_w3, new_w1)
