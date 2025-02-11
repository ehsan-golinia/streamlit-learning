import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from vega_datasets import data

st.title("🔷 st.bar_chart()")

st.divider()

st.write('''
- Display an area chart
''')

st.divider()

code = '''
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)

st.divider()

code = '''
chart_data = pd.DataFrame(
    {
        "col1": np.random.randn(20),
        "col2": np.random.randn(20),
        "col3": np.random.choice(["A", "B", "C"], 20),
    }
)

st.area_chart(chart_data, x="col1", y="col2", color="col3")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

chart_data = pd.DataFrame(
    {
        "col1": np.random.randn(20),
        "col2": np.random.randn(20),
        "col3": np.random.choice(["A", "B", "C"], 20),
    }
)

st.area_chart(chart_data, x="col1", y="col2", color="col3")

st.divider()

code = '''
chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=["col1", "col2", "col3"]
)

st.area_chart(
    chart_data,
    x="col1",
    y=["col2", "col3"],
    color=["#FF0000", "#0000FF"],  # Optional
)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=["col1", "col2", "col3"]
)

st.area_chart(
    chart_data,
    x="col1",
    y=["col2", "col3"],
    color=["#FF0000", "#0000FF"],  # Optional
)

st.divider()

code = '''
source = data.unemployment_across_industries()

st.area_chart(source, x="date", y="count", color="series", stack="center")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

source = data.unemployment_across_industries()

st.area_chart(source, x="date", y="count", color="series", stack="center")

