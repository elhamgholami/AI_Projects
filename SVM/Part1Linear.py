
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from sklearn import svm

def f1(x):
    return math.sin(math.log(x))

def f2(x):
    return -1*math.log(x)
    
#Random dataset
# np.random.seed(0)
# X = np.r_[np.random.randn(20, 1) - [2, 2], np.random.randn(20, 1) + [2, 2]]
# Y = [0] * 20 + [1] * 20
# X = np.array([1, 5, 1.5, 8, 1, 9 , 2, 7, 8.7, 2.3, 5.5, 7.7, 6.1 , 9.3 , 5.4 , 2.33 , 20.32])
# y = np.array([f1(x) for x in X ])
# training_X = X
# training_y = [0]*20 + [1]*20

#Generate using function
X = np.array([ x for x in range(1,21)])
y = np.array([f1(x) for x in X[:10]] + [f2(x) for x in X[:10]])
training_X = np.vstack((X, y)).T
training_y = [1] * 10 + [0] *10
plt.scatter(X, y)
plt.show()
# figure number
fignum = 1

# fit the model
for penalty in [0.05, 1, 10]:

    clf = svm.SVC(kernel="linear", C=penalty)
    clf.fit(training_X, training_y)

    # get the separating hyperplane
    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(-5, 5)
    yy = a * xx - (clf.intercept_[0]) / w[1]

    margin = 1 / np.sqrt(np.sum(clf.coef_**2))
    yy_down = yy - np.sqrt(1 + a**2) * margin
    yy_up = yy + np.sqrt(1 + a**2) * margin

    # plot the line, the points, and the nearest vectors to the plane
    plt.figure(fignum, figsize=(4, 3))
    plt.clf()
    plt.plot(xx, yy, "k-")
    plt.plot(xx, yy_down, "k--")
    plt.plot(xx, yy_up, "k--")

    plt.scatter(
        clf.support_vectors_[:, 0],
        clf.support_vectors_[:, 1],
        s=80,
        facecolors="none",
        zorder=10,
        edgecolors="k",
        cmap=cm.get_cmap("RdBu"),
    )
    plt.scatter(
        training_X[:, 0], training_X[:, 1], c=training_y, zorder=10, cmap=cm.get_cmap("RdBu"), edgecolors="k"
    )

    fignum = fignum + 1

plt.show()