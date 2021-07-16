import numpy as np
import matplotlib.pyplot as plt
from utils import *
# from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression

x,y = get_gen_data()
print(x.shape)
print(y.shape)
x = x.reshape(-1,1)
y = y.reshape(-1,1)
model = LinearRegression()
model.fit(x,y)
print("Sklearn model score is",model.score(x,y))
print("Sklearn model weights",model.coef_)
print("Sklearn model Intercept", model.intercept_)
