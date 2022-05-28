import streamlit as st
import joblib
from PIL import Image
import tensorflow as tf
import numpy as np
from dictionary import *
import pandas as pd
import cv2
import tempfile

MODEL = tf.keras.models.load_model("models/efficientnet_b0/model_final_101_recycling_fp32")

pred = open("pred.txt", "w")
acc = open("acc.txt", "w")

def app():      

    st.write("Please connect your camera to begin scanning items")

    btn = st.camera_input("")

    if btn:
        user_inputs, confidence = run_algorithm(
            btn,
           )

        output = user_inputs

        pred.write(str(user_inputs))


        confidence = float(confidence)
        acc.write(str(confidence)[0:5])
        acc.close()
        pred.close()
        """print(str(user_inputs))
        print(str(confidence))"""

    
def run_algorithm(button: bytes,
                  ):
            
    """Runs the neural network algorithm."""
    button = read_image(button)
    print(button)
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