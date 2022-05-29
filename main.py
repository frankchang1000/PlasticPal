"""
Runs the Multiapp Application.

MIT License (MIT) Copyright (c) 2022 frankchang1000, IdeaKing, and other contributors
"""
import tensorflow as tf

from multiapp import MultiApp
from src.apps import app1, app2  # import your app modules here

main = MultiApp()

# Add all your application here
main.add_app("Capture", app1.app)
main.add_app("Analyze", app2.app)
# The main app
main.run()
