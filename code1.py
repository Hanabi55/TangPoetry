#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time   :2021 2021/4/20 19:15
@Author :Hanabi55
@File   :peom_package.py
"""
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense, LSTM, Embedding, Dropout
import matplotlib.pyplot as plt
import os
from trainData import x_train, y_train, x_test, y_test, w_to_id, id_to_w
import random

randomSeed = random.randint(1,10)
np.random.seed(randomSeed)
np.random.shuffle(x_train)
np.random.seed(randomSeed)
np.random.shuffle(y_train)
tf.random.set_seed(randomSeed)

x_train = np.array(x_train)
y_train = np.array(y_train)
x_train = np.reshape(x_train, (len(x_train), 16))
x_test = np.array(x_test)
y_test = np.array(y_test)
x_test = np.reshape(x_test, (len(x_test), 16))

model = tf.keras.Sequential([
    Embedding(4395, 2),
    LSTM(100, return_sequences=True),
    Dropout(0.2),
    LSTM(120),
    Dropout(0.2),
    Dense(4395, activation='softmax')
])

model.compile(optimizer=tf.keras.optimizers.Adam(0.005),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['sparse_categorical_accuracy'])

checkpoint_save_path = "./checkpoint1/run_embedding_lprel.ckpt"

if os.path.exists(checkpoint_save_path + '.index'):
    print('------------load the model--------------')
    model.load_weights(checkpoint_save_path)

cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_save_path,
                                                 save_weights_only=True,
                                                 save_best_only=True,
                                                 monitor='loss')

history = model.fit(x_train, y_train, batch_size=32, epochs=50, validation_data=(x_test, y_test), validation_freq=1,
                    callbacks=[cp_callback])

model.summary()

f_write = open('./weights.txt', 'w')
for v in model.trainable_variables:
    f_write.write(str(v.name) + '\n')
    f_write.write(str(v.shape) + '\n')
    f_write.write(str(v.numpy()) + '\n')
f_write.close()

try:
# 可视化
    acc = history.history['sparse_categorical_accuracy']
    loss = history.history['loss']

    plt.subplot(1, 2, 1)
    plt.plot(acc, label='Training Accuracy')
    plt.title('Training Accuracy')
    plt.legend()

    plt.subplot(1, 2, 1)
    plt.plot(acc, label='Training Loss')
    plt.title('Training Loss')
    plt.legend()
    plt.show()
except:
    pass

peom_test = input("输入例诗：")
inputPeom = []
for i in peom_test:
    inputPeom.append(w_to_id[i])
# 输入进行预测
for i in range(32):
    inputPeom1 = np.reshape(inputPeom, (1, 16))
    result = model.predict(inputPeom1)
    predicted_next_w = tf.argmax(result, axis=1)
    predicted_next_w = int(predicted_next_w)
    inputPeom.pop(0)
    inputPeom.append(int(predicted_next_w))
    print(id_to_w[int(predicted_next_w)],end='')