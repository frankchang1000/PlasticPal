import streamlit as st
import joblib
from PIL import Image
import tensorflow as tf
import numpy as np
from dictionary import *
import pandas as pd
import cv2

MODEL = tf.keras.models.load_model("models/efficientnet_b0/model_final_101_recycling_fp32")


def app():      

    st.write("Please connect your camera to begin scanning items")

    btn = st.camera_input("")

    if btn:
        user_inputs = run_algorithm(
            btn,
           )

        output = user_inputs
        print(user_inputs)

    
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
    return label_val

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