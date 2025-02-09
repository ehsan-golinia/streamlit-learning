import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

st.title("🔷 st.checkbox()")

st.divider()

st.write('''
- Display a checkbox widget''')

st.divider()

code = '''
agree = st.checkbox("I agree")

st.write("Checkbox = ", agree)

if agree:
    st.write(":smile:" * 6)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

agree = st.checkbox("I agree")

st.write("Checkbox = ", agree)

if agree:
    st.write(":smile:" * 6)

st.divider()

code = '''
check = st.checkbox("Uncheck to remove cake", value=True)

st.write("Checkbox = ", check)

if check:
    st.write(":cake:" * 6)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

check = st.checkbox("Uncheck to remove cake", value=True)

st.write("Checkbox = ", check)

if check:
    st.write(":cake:" * 6)
