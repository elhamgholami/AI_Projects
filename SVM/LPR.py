from sklearn.model_selection import train_test_split
from sklearn import svm, metrics
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import numpy as np
import os

input_images = []
input_images_label = []


def readImagesFromFile():
    global input_images, input_images_label
    folders = ["2", "3", "7", "S", "W"]
    for folder in folders:
        for root, directory, files in os.walk("persian_LPR/" + folder):
            for image in files:
                input_images_label.append(folder)
                img = imageio.imread("persian_LPR/" + folder + "/" + image)
                color_features = img.flatten()
                image_features = np.hstack(color_features)
                input_images.append(image_features)


def predict():
    x_train, x_test, y_train, y_test = train_test_split(input_images, input_images_label, test_size=0.2)

    classifier = svm.SVC(kernel='poly' , C=1)
    classifier.fit(x_train, y_train)
    prediction = classifier.predict(x_test)

    print("Accuracy of Support vector Machine, %s:\n%s\n" % (
    classifier, metrics.classification_report(y_test, prediction)))



def startClassification():
    readImagesFromFile()
    predict()

startClassification()