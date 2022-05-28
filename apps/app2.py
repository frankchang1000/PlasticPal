import re
import streamlit as st
import joblib
from PIL import Image
import tensorflow as tf
import numpy as np
from dictionary import *
import pandas as pd
from apps import app1 as app1
import inflection


def app():      


    col1, col2  = st.columns(2)

    pred = open("pred.txt", "r")
    acc = open("acc.txt", "r")

    detected = pred.read()

    with col1:
        st.header("Classified Object: ")
        underscore = inflection.underscore(detected)
        st.subheader(inflection.humanize(underscore))

    with col2:
        st.header("Confidence: ")
        st.subheader(acc.read())


    if (recycleStatus[detected] == 1):
        #st.write("This item can be recycled!")
        st.image("data/2.jpg", use_column_width=True)
    elif (recycleStatus[detected] == 0):
        #st.write("This item cannot be recycled")
        st.image("data/1.jpg", use_column_width=True)
    else:
        #st.write("This item might be recyclable")
        st.image("data/3.jpg", use_column_width=True)


    pred.close()
    acc.close()
    