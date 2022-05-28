import streamlit as st
from multiapp import MultiApp
from apps import app1, app2# import your app modules here

main = MultiApp()


# Add all your application here
main.add_app("Capture", app1.app)
main.add_app("Analyze", app2.app)
# The main app
main.run()