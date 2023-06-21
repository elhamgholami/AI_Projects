#import libraries
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import random
from numpy import *
import math

###Part2
#---------------------------------------------

###functions:
##f1(x) = sin(4x)
##f2(x) = 3x^2 - sin(x) + tanh(x)/x^3
##f3(x) = 5xrad(x) /log(x)

def f3(x) :
    return sin(4*x)
def f2(x) :
    return 3*(x*x) - sin(x) + tanh(x)/(x*x*x)
def f1(x) :
    return sqrt(abs(x)) * x  

def add_noise (item ,rate ):
    item += rate 
    return item

Xs = arange(-pi , pi , 0.005)

Ys = [f1(x) for x in Xs]


x_train, x_test, y_train, y_test = train_test_split(Xs, Ys, test_size=0.3)
for i in range(len(y_train)):
    if random.randint(100, 10000) %2 == 0 :
        y_train[i] = add_noise(y_train[i], 0.1)

x_train = x_train.reshape(-1,1)#making array 1D???
x_test = x_test.reshape(-1,1)

##construsting Neural Network
mlp = MLPRegressor(
    hidden_layer_sizes=[ 100 , 200 , 300 , 100 , 80 ],
    activation='relu' , 
    alpha= 0.0001 ,
    max_iter =  10000, #1 , 10 , 100 , 1000 , 100000 has been tried . best = 10000
)

mlp.fit(x_train,y_train)
result = mlp.predict(x_test)

##plotting result
plt.figure()
plt.plot(Xs, Ys , 'b')

plt.plot(x_test , y_test , 'x')

plt.plot(x_test , result , 'ro')
plt.show()

##calculate error
mse = mean_squared_error(y_test, result)
print(f"Mean Squared Error : {mse}" )


