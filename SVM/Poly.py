import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from sklearn import svm
from sklearn.datasets import make_moons

X, y = make_moons(n_samples=40, noise=0.4)
plt.scatter(X[:, 0], X[:, 1], c=y, marker='.')
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
    
    # plot decision boundary
    ax.contour(X, Y, P,
               levels=[0], alpha=0.5,
               linestyles=['-'])


# fit the model
for k in ['poly', 'sigmoid', 'rbf']:

    nonlinear_clf = svm.SVC(kernel=k, C=1)
    nonlinear_clf.fit(X, y)
    plt.scatter(X[:, 0], X[:, 1], c=y, marker='.')
    plot_decision_boundary(nonlinear_clf)
    plt.scatter(nonlinear_clf.support_vectors_[:, 0], nonlinear_clf.support_vectors_[:, 1], s=50, lw=1, facecolors='none')
    plt.title(k)
    plt.show()