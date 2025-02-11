import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from vega_datasets import data

st.title("🔷 st.scatter_chart()")

st.divider()

st.write('''
- Display a scatterplot chart
''')

st.divider()

code = '''
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.scatter_chart(chart_data)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.scatter_chart(chart_data)

st.divider()

code = '''
chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=["col1", "col2", "col3"]
)
chart_data["col4"] = np.random.choice(["A", "B", "C"], 20)

st.scatter_chart(
    chart_data,
    x="col1",
    y="col2",
    color="col4",
    size="col3",
)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=["col1", "col2", "col3"]
)
chart_data["col4"] = np.random.choice(["A", "B", "C"], 20)

st.scatter_chart(
    chart_data,
    x="col1",
    y="col2",
    color="col4",
    size="col3",
)

st.divider()

code = '''
chart_data = pd.DataFrame(
    np.random.randn(20, 4), columns=["col1", "col2", "col3", "col4"]
)

st.scatter_chart(
    chart_data,
    x="col1",
    y=["col2", "col3"],
    size="col4",
    color=["#FF0000", "#0000FF"],  # Optional
)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

chart_data = pd.DataFrame(
    np.random.randn(20, 4), columns=["col1", "col2", "col3", "col4"]
)

st.scatter_chart(
    chart_data,
    x="col1",
    y=["col2", "col3"],
    size="col4",
    color=["#FF0000", "#0000FF"],  # Optional
)
