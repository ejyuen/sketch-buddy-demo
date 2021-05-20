import streamlit as st
import streamlit.components.v1 as components

import numpy as np
import tensorflow as tf
import cv2 

class_names = np.genfromtxt("labels.txt", dtype="str", delimiter='\n')
for i in range(len(class_names)):
  class_names[i] = ' '.join(class_names[i].split(' ')[1::])
np.set_printoptions(suppress=True)

model = tf.keras.models.load_model('keras_model.h5', compile = False)

def get_image_classification(image_data):
    img = image_data
    img32 = np.float32(img)
    bgr = cv2.cvtColor(img32, cv2.COLOR_BGRA2BGR)
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

    rgb = cv2.resize(rgb,(224,224)).astype('float32')
    rgb = np.reshape(rgb,(1,224,224,3))
    rgb = rgb / 255

    predictions = model.predict(rgb)[0]
    classification = class_names[np.argmax(predictions)]
    return classification, predictions