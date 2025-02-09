import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

st.title("🔷 st.number_input()")

st.divider()

st.write('''
- Display a numeric input widget''')

st.divider()

code = '''number = st.number_input("Insert a number")
st.write("The current number is ", number)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

number = st.number_input("Insert a number")
st.write("The current number is ", number)

st.divider()

code = '''number = st.number_input(
    "Insert a number", value=None, placeholder="Type a number..."
)
st.write("The current number is ", number)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

number = st.number_input(
    "Insert a number", value=None, placeholder="Type a number..."
)
st.write("The current number is ", number)
