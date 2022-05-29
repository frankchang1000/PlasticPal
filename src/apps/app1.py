"""
Displays webpage for inputting an image.
"""
import cv2

import numpy as np
import streamlit as st
import tensorflow as tf

from src.dictionary import *

MODEL = tf.keras.models.load_model("models/efficientnet_b0/model_final_101_recycling_fp32")

def app():      
    #st.write("Please connect your camera to begin scanning items")
    btn = st.camera_input("")
    st.write("After taking a photo, use the dropdown to change to image classification")
    if btn:
        pred = open("users/pred.txt", "w")
        acc = open("users/acc.txt", "w")
        user_inputs, confidence = run_algorithm(btn)
        pred.write(str(user_inputs))
        confidence = float(confidence)
        acc.write(str(confidence)[0:5])
        acc.close()
        pred.close()


def run_algorithm(button: bytes):
    """Runs the neural network algorithm using user input image."""
    button = read_image(button)
    button = cv2.resize(np.array(button), (128, 128))
    outputs = MODEL(tf.expand_dims(button, axis=0), training=False)
    outputs = tf.squeeze(outputs, axis=0)
    index_val = tf.argmax(outputs, axis=0)
    label_val = LABELS[index_val-1]
    confidence = outputs[index_val]
    return label_val, confidence


def read_image(user_img):
    """Reads the image.
    Params:
        user_img: bytes
            The image from the camera.
    Returns:
        image: np.array
    """
    if user_img is not None:
        bytes_data = user_img.getvalue()
        img_tensor = tf.io.decode_image(bytes_data, channels=3)
        return img_tensor

