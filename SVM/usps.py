import numpy as np # linear algebra
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn import svm
import h5py 
import os
from functools import reduce
def hdf5(path, data_key = "data", target_key = "target", flatten = True):
    with h5py.File(path, 'r') as hf:
        train = hf.get('train')
        X_tr = train.get(data_key)[:]
        y_tr = train.get(target_key)[:]
        test = hf.get('test')
        X_te = test.get(data_key)[:]
        y_te = test.get(target_key)[:]
        if flatten:
            X_tr = X_tr.reshape(X_tr.shape[0], reduce(lambda a, b: a * b, X_tr.shape[1:]))
            X_te = X_te.reshape(X_te.shape[0], reduce(lambda a, b: a * b, X_te.shape[1:]))
    return X_tr, y_tr, X_te, y_te

X_tr, y_tr, X_te, y_te = hdf5("usps.h5")

num_samples = 10
num_classes = len(set(y_tr))

classes = set(y_tr)
num_classes = len(classes)
fig, ax = plt.subplots(num_samples, num_classes, sharex = True, sharey = True, figsize=(num_classes, num_samples))

for label in range(num_classes):
    class_idxs = np.where(y_tr == label)
    for i, idx in enumerate(np.random.randint(0, class_idxs[0].shape[0], num_samples)):
        ax[i, label].imshow(X_tr[class_idxs[0][idx]].reshape([16, 16]), 'gray')
        ax[i, label].set_axis_off()

#Linear svm

# lsvm = svm.LinearSVC(C = 0.05)
# lsvm.fit(X_tr, y_tr)

# preds = lsvm.predict(X_te)

#Poly svm
# p = svm.SVC(kernel="poly", C=10)#100 , 0.01 , 0.001
# p.fit(X_tr , y_tr)
# preds = p.predict(X_te)

#Rbf svm 
p = svm.SVC(kernel="rbf", C=100)#0.01, 1, 10, 100, 1000
p.fit(X_tr , y_tr)
preds = p.predict(X_te)

#Sigmoid svm
# p = svm.SVC(kernel="sigmoid", C=10)#0.01, 1, 10, 100, 1000
# p.fit(X_tr , y_tr)
# preds = p.predict(X_te)
#best machine using different kernel and parameters

# param_grid={'C':[0.1,1,10,100],
# 			'gamma':[0.0001,0.001,0.1,1],
# 			'kernel':['rbf' , 'poly']}

# # Creating a support vector classifier
# svc=svm.SVC(probability=True)

# # Creating a model using GridSearchCV with the parameters grid
# model=GridSearchCV(svc,param_grid)

# model.fit(X_tr, y_tr)
# preds = model.predict(X_te)

accuracy = sum((preds == y_te))/len(y_te)
print("Accuracy of Support vector Machine, ", accuracy)
