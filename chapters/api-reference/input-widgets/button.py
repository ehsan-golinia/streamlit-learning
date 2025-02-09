import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

st.title("🔷 st.button()")

st.divider()

st.write('''
- Display a button widget''')

st.divider()

code = '''reset_button = st.button("Reset", type="primary")
st.write("Reset button = ", reset_button)

if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

reset_button = st.button("Reset", type="primary")
st.write("Reset button = ", reset_button)
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")

st.divider()

code = '''left, middle, right = st.columns(3)

if left.button("Plain button", use_container_width=True):
    left.markdown("You clicked the plain button.")

if middle.button("Emoji button", icon="😃", use_container_width=True):
    middle.markdown("You clicked the emoji button.")

if right.button("Material button", icon=":material/mood:", use_container_width=True):
    right.markdown("You clicked the Material button.")'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

left, middle, right = st.columns(3)

if left.button("Plain button", use_container_width=True):
    left.markdown("You clicked the plain button.")

if middle.button("Emoji button", icon="😃"):
    middle.markdown("You clicked the emoji button.")

if right.button("Material button", icon=":material/mood:", use_container_width=True):
    right.markdown("You clicked the Material button.")
