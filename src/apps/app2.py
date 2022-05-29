"""
Displays webpage with detected object and confidence.
"""
import inflection
import streamlit as st

from src.dictionary import *
from src.apps import app1 as app1


def app():
    col1, col2 = st.columns(2)
    with open("users/pred.txt", "r") as pred:
        detected = pred.read()

    with col1:
        st.header("Classified Object: ")
        underscore = inflection.underscore(detected)
        st.subheader(inflection.humanize(underscore))

    with col2:
        st.header("Confidence: ")
        with open("users/acc.txt", "r") as acc:
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

    # pred.close()
    # acc.close()
