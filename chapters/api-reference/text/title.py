import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from vega_datasets import data

st.title("🔷 st.title()")

st.divider()

st.write('''
- Display text in title formatting
''')

st.divider()

code = '''
st.title("This is a title")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")'''
st.code(code, language="python")

st.markdown(":orange[Output:]")


st.title("This is a title")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")
