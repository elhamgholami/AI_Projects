
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from sklearn import svm
from sklearn import datasets

circle_X, circle_y = datasets.make_circles(n_samples=300, noise=0.05)
plt.scatter(circle_X[:, 0], circle_X[:, 1], c=circle_y, marker='.')
plt.show()

def plot_decision_boundary(model, ax=None):
    if ax is None:
        ax = plt.gca()
        
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    x = np.linspace(xlim[0], xlim[1], 30)
    y = np.linspace(ylim[0], ylim[1], 30)
    Y, X = np.meshgrid(y, x)

    xy = np.vstack([X.ravel(), Y.ravel()]).T
    
    P = model.decision_function(xy).reshape(X.shape)
    
    ax.contour(X, Y, P,
               levels=[0], alpha=0.5,
               linestyles=['-'])



# fit the model
for penalty in [1 , 10]:

    nonlinear_clf = svm.SVC(kernel="rbf", C=penalty)
    nonlinear_clf.fit(circle_X, circle_y)

    plt.scatter(circle_X[:, 0], circle_X[:, 1], c=circle_y, s=50)
    plot_decision_boundary(nonlinear_clf)
    plt.scatter(nonlinear_clf.support_vectors_[:, 0], nonlinear_clf.support_vectors_[:, 1], s=50, lw=1, facecolors='none')
    plt.show()