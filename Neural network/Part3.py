import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error


import numpy as np

def F1(x,y):
    return math.sin(5*x)*math.cos(5*y)/5
    # return math.sin(10*(x*x+y*y))/10
    # return 1/(15*(x*x+y*y))
    # return np.exp(-(np.square(x) + np.square(y))/0.1)

x = np.arange(-1,1,0.04)
# y = np.arange(-1,1,0.06)
xy = [(i,j) for i in x for j in x]
out = [F1(p[0],p[1]) for p in xy]
x_train, x_test, y_train, y_test = train_test_split(xy, out)

fig = plt.figure()
ax = fig.gca(projection='3d')

# plot train data points
x1_vals = np.array([p[0] for p in x_train])
x2_vals = np.array([p[1] for p in x_train])

# ax.scatter(x1_vals, x2_vals, y_train)

# plot test data points
x1_vals = np.array([p[0] for p in x_test])
x2_vals = np.array([p[1] for p in x_test])

ax.scatter(x1_vals, x2_vals, y_test, c='red')

mlp = MLPRegressor(
    # hidden_layer_sizes=[ 100 , 1000 ,  80 ],
    # hidden_layer_sizes=[ 100 , 80 ],
    # hidden_layer_sizes=[1 , 2 , 3 , 5] ,
    # hidden_layer_sizes=[5 , 8 , 10 , 1] ,
    hidden_layer_sizes=[56 , 100 , 60] ,
    activation='relu' , 
    # activation='logistic' , 
    # activation = 'identity' ,
    alpha= 0.0001 ,
    max_iter =  10000, #1 , 10 , 100 , 1000 , 100000 has been tried . best = 10000
)
# train network
mlp.fit(x_train,y_train)

# test
predictions = mlp.predict(x_test)

mse = mean_squared_error(y_test, predictions )
ax.scatter(x1_vals, x2_vals, predictions, c='green' , marker='x')
print(f"Mean Squared Error : {mse}" )

plt.show()