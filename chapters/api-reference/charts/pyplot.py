import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from vega_datasets import data

st.title("🔷 st.pyplot")

st.divider()

st.write('''
- Display a matplotlib.pyplot figure
- You must install `matplotlib` to use this command
''')

st.divider()

code = '''
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
