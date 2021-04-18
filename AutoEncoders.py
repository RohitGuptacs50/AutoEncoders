# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E-3WCT5WFmiZOMMVpnm8BdnE7rbKhpWU

Applications could be in time _series data to map the input to the output for regular data and if any anomaly in the data occurs then, the model trained on the regular input will not generate the output.
Eg, ECG data, data of mechanical devices, like pump etc
"""

import tensorflow as tf
from tensorflow import keras
import cv2
import numpy as np

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train / 255.0
x_test = x_test / 255.0

"""It compresses the number of input features and reduces the noise """

import matplotlib.pyplot as plt
plt.imshow(x_train[0], cmap = 'gray')

x_train[0]

x_train[0].shape



"""Build the encoder"""

encode_input = keras.Input(shape=(28, 28, 1), name = 'img')
x = keras.layers.Flatten()(encode_input)
encode_output = keras.layers.Dense(64, activation='relu')(x)    # reduced to 64 features from 128(28 * 28)



encode = keras.Model(encode_input, encode_output, name = 'encoder')

"""Build the decoder"""

decode_input = keras.layers.Dense(64, activation='relu')(encode_output)

x = keras.layers.Dense(784, activation='relu')(decode_input)
decode_output = keras.layers.Reshape((28, 28, 1))(x)

opt = tf.keras.optimizers.Adam(lr = 0.001, decay = 1e-6)
autoencoder = keras.Model(encode_input, decode_output, name = 'autoencoder')    # the idea is to map the input to the output

autoencoder.summary()

autoencoder.compile(opt, loss='mse')

epochs = 5

for epoch in range(epochs):
  history = autoencoder.fit(x_train, x_train, epochs = 1, batch_size=32,
                            validation_split=0.10)
  autoencoder.save(f'/content/drive/MyDrive/Colab Notebooks/AutoEncoders_Sentdex/saved models/AE-{epoch + 1}.model')

example = encode.predict([x_test[0].reshape(-1, 28, 28, 1)])
print(example[0].shape)
print(example[0])

plt.imshow(example[0].reshape((8, 8)), cmap = 'gray')

plt.imshow(x_test[0], cmap = 'gray')







