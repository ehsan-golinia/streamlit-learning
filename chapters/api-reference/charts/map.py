import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from vega_datasets import data

st.title("🔷 st.map")

st.divider()

st.write('''
- Display a map with a scatterplot overlaid onto it
''')

st.divider()

code = '''
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)
st.map(df, size=20, color="#0044ff")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)
st.map(df, size=20, color="#0044ff")

st.divider()

code = '''
df = pd.DataFrame(
    {
        "col1": np.random.randn(1000) / 50 + 37.76,
        "col2": np.random.randn(1000) / 50 + -122.4,
        "col3": np.random.randn(1000) * 100,
        "col4": np.random.rand(1000, 4).tolist(),
    }
)

st.map(df, latitude="col1", longitude="col2", size="col3", color="col4")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

df = pd.DataFrame(
    {
        "col1": np.random.randn(1000) / 50 + 37.76,
        "col2": np.random.randn(1000) / 50 + -122.4,
        "col3": np.random.randn(1000) * 100,
        "col4": np.random.rand(1000, 4).tolist(),
    }
)

st.map(df, latitude="col1", longitude="col2", size="col3", color="col4")
