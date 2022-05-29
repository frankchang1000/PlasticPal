"""
Displays webpage with detected object and confidence.
"""
import inflection
import streamlit as st

from src.dictionary import *
from src.apps import app1 as app1


def app():      


    col1, col2  = st.columns(2)

    pred = open("users/pred.txt", "r")
    acc = open("users/acc.txt", "r")

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
        st.image("docs/recycle.jpg", use_column_width=True)
    elif (recycleStatus[detected] == 0):
        #st.write("This item cannot be recycled")
        st.image("docs/not_recycle.jpg", use_column_width=True)
    else:
        #st.write("This item might be recyclable")
        st.image("docs/maybe.jpg", use_column_width=True)

    pred.close()
    acc.close()
