#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time   :2021 2021/4/27 17:18
@Author :Hanabi55
@File   :code2.py
"""
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense, GRU, Embedding, Dropout
import matplotlib.pyplot as plt
import os


def create_peom(num_epochs):
    from trainData import x_train, y_train, x_test, y_test, w_to_id, id_to_w

    os.environ["CUDA_VISIBLE_DEVICES"] = "0"

    np.random.seed(10)
    np.random.shuffle(x_train)
    np.random.seed(10)
    np.random.shuffle(y_train)
    tf.random.set_seed(10)

    x_train = np.array(x_train)
    y_train = np.array(y_train)
    x_train = np.reshape(x_train, (len(x_train), 32))
    x_test = np.array(x_test)
    y_test = np.array(y_test)
    x_test = np.reshape(x_test, (len(x_test), 32))

    model = tf.keras.Sequential([
        Embedding(4396, 200),
        GRU(600, return_sequences=True),
        Dropout(0.5),
        GRU(750),
        Dropout(0.5),
        Dense(4396, activation='softmax')
    ])

    model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
                  metrics=['sparse_categorical_accuracy'])

    checkpoint_save_path = "./checkpoint/run_embedding_lprel.ckpt"

    if os.path.exists(checkpoint_save_path + '.index'):
        print('------------load the model--------------')
        model.load_weights(checkpoint_save_path)

    cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_save_path,
                                                     save_weights_only=True,
                                                     save_best_only=True,
                                                     monitor='loss')

    history = model.fit(x_train, y_train, batch_size=32, epochs=num_epochs, validation_data=(x_test, y_test),
                        validation_freq=1,
                        callbacks=[cp_callback])

    model.summary()

    f_write = open('./weights.txt', 'w')
    for v in model.trainable_variables:
        f_write.write(str(v.name) + '\n')
        f_write.write(str(v.shape) + '\n')
        f_write.write(str(v.numpy()) + '\n')
    f_write.close()

    # 可视化
    try:
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
    printPeom = []
    for i in peom_test:
        inputPeom.append(w_to_id[i])
    # 输入进行预测
    for i in range(16):
        inputPeom_tmp = []
        inputPeom_tmp = inputPeom + inputPeom_tmp
        while len(inputPeom_tmp) != 32:
            inputPeom_tmp.append(0)
        inputPeom_tmp = np.reshape(inputPeom_tmp, (1, 32))
        result = model.predict(inputPeom_tmp)
        predicted_next_w = tf.argmax(result, axis=1)
        predicted_next_w = int(predicted_next_w)
        inputPeom.append(predicted_next_w)
        printPeom.append(predicted_next_w)
        print(id_to_w[predicted_next_w], end='')

    inputPeom = printPeom
    for i in range(16):
        inputPeom_tmp = []
        inputPeom_tmp = inputPeom + inputPeom_tmp
        while len(inputPeom_tmp) != 32:
            inputPeom_tmp.append(0)
        inputPeom_tmp = np.reshape(inputPeom_tmp, (1, 32))
        result = model.predict(inputPeom_tmp)
        predicted_next_w = tf.argmax(result, axis=1)
        predicted_next_w = int(predicted_next_w)
        inputPeom.append(predicted_next_w)
        print(id_to_w[predicted_next_w], end='')
    print()
    return 0
