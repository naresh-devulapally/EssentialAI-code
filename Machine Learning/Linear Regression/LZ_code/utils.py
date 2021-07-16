import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_data_1d():
    X = []
    Y = []

    for line in open('data/data_1d.csv'):
        x,y = line.split(',')
        X.append(float(x))
        Y.append(float(y))

    X = np.array(X)
    Y = np.array(Y)

    return X,Y

def get_gen_data(N = 200, m = 0.5, b = -0.5):
    x = np.random.random(N)*10-5
    y = m*x+b + np.random.random(N)
    return x,y

def moore_data():
    data = pd.read_csv('data/moore.csv', header = None).values
    X = data[:,0]
    Y = data[:,1]
    Y = np.log(Y)
    mx = X.mean()
    sx = X.std()
    my = Y.mean()
    sy = Y.std()
    X = (X - mx)/sx
    Y = (Y - my)/sy
    return X,Y,sx,sy

def get_2d_data():
    X = []
    Y = []
    for line in open('data/data_2d.csv'):
        x1,x2,y= line.split(",")
        X.append([1,float(x1),float(x2)])
        Y.append(float(y))
    X = np.array(X)
    Y = np.array(Y)
    return X,Y

def get_poly_data():
    X = []
    Y = []
    for line in open('data/data_poly.csv'):
        x,y = line.split(',')
        x = float(x)
        X.append([1,x,x*x])
        Y.append(float(y))
    X = np.array(X)
    Y = np.array(Y)
    return X,Y
