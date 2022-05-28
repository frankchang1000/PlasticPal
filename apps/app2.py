import streamlit as st
import joblib
from PIL import Image
import tensorflow as tf
import numpy as np
from dictionary import *
import pandas as pd
from apps import app1 as app1


def app():      


    pred = open("pred.txt", "r")
    acc = open("acc.txt", "r")
    st.write("Classified Object: " + pred.read())
    st.write("Confidence: " + acc.read())
    pred.close()
    acc.close()
    