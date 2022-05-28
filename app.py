import streamlit as st
import joblib
from PIL import Image
import tensorflow as tf



#load the model
print("Loading models...")
MODEL = tf.keras.models.load_model("data/model_good")



def main():      
    st.header("Welcome to Plastic Pal!")

    st.write("Please connect your camera to begin scanning items")

    button = st.camera_input("")

if __name__ == '__main__':
    main()