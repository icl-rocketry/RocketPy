
'''
ICLR RocketPy - Frontend
Maintained by Raihaan Usman

The face of RocketPy! Uses Flask and Streamlit to provide a web interface for the RocketPy workflow.

Full usage notes are available at https://rpycore.readthedocs.io/en/latest/

'''

from flask import Flask, render_template, request, jsonify          # The nice Flask web framework
import streamlit as st                                              # The pretty Streamlit web framework



app = Flask(__name__)


if not hasattr(st, 'already_started_server'):
    # Hack the fact that Python modules (like st) only load once to
    # keep track of whether this file already ran.
    st.already_started_server = True

    st.write('''
        The first time this script executes it will run forever because it's
        running a Flask server.

        Just close this browser tab and open a new one to see your Streamlit
        app.
    ''')

    app = Flask(__name__)

    @app.route('/login')
    def serve_foo():
        # return 'This page is served via Flask!'
        return 'yey'

    app.run(port=8888)

st.write(
"""
# RocketPy.
The official rocket maker.

"""
)

# # We'll never reach this part of the code the first time this file executes!

# # Your normal Streamlit app goes here:
# x = st.slider('Pick a number')
# st.write('You picked:', x)