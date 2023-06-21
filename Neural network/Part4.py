#import libraries
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from numpy import *
import math

###Part4
#---------------------------------------------

x_train = [-4.0 , -3.9 , -3.8 , -3.0 , -2.9 , -2.2 , -2.1,-2 , -1.3 ,-0.8 , -0.3 , 0 , 0.7 , 0.9 , 1.3 , 1.75 ,2.2 , 2.3 , 2.45 , 3.1 , 3.4 , 3.8 , 4 ]
y_train = array([2.35 , 2.1 , 2.2 , 3.45 , 2.75 , 3.4 , 3.95 , 5.12 , 6.01 , 5.09 , 4 , 3.3 , 3.2 , 3.45 , 3.1 , 2.3 , 3 , 4 , 5.3 , 5.95 , 5 , 3.89 , 3.23 ])
x_train = array(x_train)
x_train = x_train.reshape(-1,1)
x_test = [-3.7 , -2.95 , -2.23 , -2.3 ,  -1.7 , -1.3 , -0.6 , -0.4 , 0.1 , 1.1 , 1.4 , 2 , 2.32 ,3.3 ]
y_test = array([1.2 , 2.95 , 2.17 , 3 , 4.45 , 5.78 , 4.88 , 3.75 , 3 , 3.83 , 2.8 , 2.65 , 4.7 , 5.3])
x_test = array(x_test).reshape(-1 , 1)
##construsting Neural Network
mlp = MLPRegressor(
    hidden_layer_sizes=[ 54 , 18 , 9 , 81],
    # activation='logistic' , 
    # activation = 'identity' ,
    activation = 'relu' ,
    alpha= 0.00015 ,
    max_iter =  8000, #1 , 10 , 100 , 1000 , 100000 has been tried . best = 10000
    
)

mlp.fit(x_train,y_train)
result = mlp.predict(x_test)

##plotting result
plt.figure()
# plt.plot(Xs, Ys , 'b')
# plt.plot(x_train , y_train , 'o')
plt.plot(x_test , y_test , 'x')
plt.plot(x_test , result , 'ro')
plt.show()

##calculate error
mse = mean_squared_error(y_test, result)
print(f"Mean Squared Error : {mse}" )


