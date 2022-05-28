import streamlit as st
import joblib
from PIL import Image
import tensorflow as tf
import numpy as np
from dictionary import *
import pandas as pd

#load the model
print("Loading models...")
MODEL = tf.keras.models.load_model("models/efficientnet_b0/model_final_101_recycling_fp32")


def page_switcher(page):
    st.session_state.runpage = page

def updatePage():
    st.header("Welcome to Plastic Pal!")
    st.image()
    btn = st.button('reset')
    if btn :
        st.session_state.runpage = main        
        st.experimental_rerun()

def main():      
    st.header("Welcome to Plastic Pal!")

    st.write("Please connect your camera to begin scanning items")

    btn = st.camera_input("")
    

    if btn:
        st.experimental_rerun() 
        updatePage()
        # rerun is needed to clear the page

        


def prediction(image: np.array,
               image_dims: tuple = (128, 128),
               labels: list = LABELS):
    """Predicts the image.
    Params:
        image: np.array
            The image.
        image_dims: tuple
            The image dimensions.
        labels: list
            The labels.
    Returns:
        preds: list
            The predictions.
    """
    image = tf.image.resize(image, image_dims)
    image = tf.image.convert_image_dtype(
        image=image, 
        dtype=tf.float32)
    image = tf.expand_dims(image, 0)
    label_index, probs = inference.run_inference(image, MODEL)
    print("Prediction label index: ", label_index)
    class_name = labels[label_index]
    return class_name, label_index, probs


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





if __name__ == '__main__':
    main()