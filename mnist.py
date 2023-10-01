# -*- coding: utf-8 -*-
"""MNIST.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rR3zZgFvLlG-PJtaTr0SOKCY7cS31MXK

Import All Required Libraries
"""

import cv2   # it will allow us to load our images into the script
import numpy as np   # used for reformatting our own images
import tensorflow as tf   # main library used to load data sets, build neural networks, train them, etc.
import matplotlib.pyplot as plt   # used for visualization

import tensorflow
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Flatten

"""Dataset load from Keras and data preparation"""

(X_train,y_train),(X_test,y_test) = keras.datasets.mnist.load_data()

import matplotlib.pyplot as plt
plt.imshow(X_train[23])

# to convert all value in between 0-1 we require to divide it 255
X_train = X_train/255
X_test = X_test/255

"""Build up the Keras Sequential Model"""

#Flattaning layer operation will be require to give 784 pixel values as input
model = Sequential()

model.add(Flatten(input_shape=(28,28))) #It will convert data into 1D --784inputs
model.add(Dense(128,activation="relu"))#no need to give inputs flatten layer will automatically gives  #here 128nodes for input layer
model.add(Dense(32,activation="relu"))
model.add(Dense(10,activation="softmax"))  #softmax bz we are having more than one nodes in output

model.summary()

model.compile(loss="sparse_categorical_crossentropy",optimizer="Adam",metrics=["accuracy"])
#in sparse categorical crossentropy we dont need to do one hot encoding

history= model.fit(X_train,y_train,epochs=25,validation_split=0.2)

y_prob = model.predict(X_test)

y_prob

y_pred = y_prob.argmax(axis=1) #Taking only one higher probablity

y_pred

from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)

"""Graphical Representation of loss, Validation loss, accuracy and Validation accuracy"""

import matplotlib.pyplot as plt

plt.plot(history.history["loss"])
plt.plot(history.history["val_loss"])

plt.plot(history.history["accuracy"])
plt.plot(history.history["val_accuracy"])

"""Testing"""

plt.imshow(X_test[0])

model.predict(X_test[0].reshape(1,28,28))

model.predict(X_test[0].reshape(1,28,28)).argmax(axis=1)

"""This prediction consists of the ten activations or probabilities from the output neurons.
Since we need to generate a result out of that, we are going to use the argmax function. This function returns the index of the highest value.
In this case this is equivalent to the digit with the highest probability or activation.
"""

