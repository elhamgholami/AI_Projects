import numpy as np
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from mpl_toolkits.mplot3d import Axes3D

#Load data
iris = datasets.load_iris()
X = iris.data[:, :1000]
Y = iris.target

X = X[np.logical_or(Y==0,Y==1)]
Y = Y[np.logical_or(Y==0,Y==1)]

model = svm.SVC(kernel='linear')
clf = model.fit(X, Y)

#Find the boundary
z = lambda x,y: (-clf.intercept_[0]-clf.coef_[0][0]*x -clf.coef_[0][1]*y) / clf.coef_[0][2]

tmp = np.linspace(-5,5,30)
x,y = np.meshgrid(tmp,tmp)

#Plot
fig = plt.figure()
ax  = fig.add_subplot(111, projection='3d')
ax.plot3D(X[Y==0,0], X[Y==0,1], X[Y==0,2], 'ob',color= 'red' )
ax.plot3D(X[Y==1,0], X[Y==1,1], X[Y==1,2], 'sr',color= 'green' )
ax.plot_surface(x, y, z(x,y), color= 'black')
ax.view_init(30, 60)
plt.title('Linear')
plt.show()