"""
Displays webpage for inputting an image.
"""

import cv2

import numpy as np
import streamlit as st
import tensorflow as tf

from main import MODEL
from src.dictionary import *


def app():
    st.write("Please connect your camera to begin scanning items.")
    btn = st.camera_input("")
    if btn:
        user_inputs, confidence = run_algorithm(btn)
        with open("users/pred.txt", "w") as pred:
            pred.write(str(user_inputs))
        confidence = float(confidence)
        with open("users/acc.txt", "w") as acc:
            acc.write(str(confidence)[0:5])
        # acc.close()
        # pred.close()


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
