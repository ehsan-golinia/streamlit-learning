import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from vega_datasets import data
import time

st.title("🔷 st.table()")

st.divider()

st.write('''
- Display a static table
''')

st.divider()

code = '''
df = pd.DataFrame(
    np.random.randn(6, 5), columns=("col %d" % i for i in range(5))
)

st.table(df)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

df = pd.DataFrame(
    np.random.randn(6, 5), columns=["col %d" % i for i in range(5)]
)

st.table(df)

st.divider()

code = '''
df = pd.DataFrame(
    {
        "Command": ["**st.table**", "*st.dataframe*"],
        "Type": ["`static`", "`interactive`"],
        "Docs": [
            "[:rainbow[docs]](https://docs.streamlit.io/develop/api-reference/data/st.dataframe)",
            "[:book:](https://docs.streamlit.io/develop/api-reference/data/st.table)",
        ],
    }
)
st.table(df)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

df = pd.DataFrame(
    {
        "Command": ["**st.table**", "*st.dataframe*"],
        "Type": ["`static`", "`interactive`"],
        "Docs": [
            "[:rainbow[docs]](https://docs.streamlit.io/develop/api-reference/data/st.dataframe)",
            "[:book:](https://docs.streamlit.io/develop/api-reference/data/st.table)",
        ],
    }
)
st.table(df)

st.divider()

code = '''
df1 = pd.DataFrame(
    np.random.randn(2, 6), columns=["col %d" % i for i in range(6)]
)

add_btn = st.button("Add Row")
my_spinner = st.spinner("Wait for it...", show_time=True)
my_table = st.table(df1)

df2 = pd.DataFrame(
    np.random.randn(2, 6), columns=["col %d" % i for i in range(6)]
)

if add_btn:
    with my_spinner:
        for i in range(6):
            time.sleep(2)
            df2 = pd.DataFrame(
                np.random.randn(1, 6), columns=["col %d" % i for i in range(6)]
            )
            my_table.add_rows(df2)

    st.success("Done!")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

df1 = pd.DataFrame(
    np.random.randn(2, 6), columns=["col %d" % i for i in range(6)]
)

add_btn = st.button("Add Row")
my_spinner = st.spinner("Wait for it...", show_time=True)
my_table = st.table(df1)

df2 = pd.DataFrame(
    np.random.randn(2, 6), columns=["col %d" % i for i in range(6)]
)

if add_btn:
    with my_spinner:
        for i in range(6):
            time.sleep(2)
            df2 = pd.DataFrame(
                np.random.randn(1, 6), columns=["col %d" % i for i in range(6)]
            )
            my_table.add_rows(df2)

    st.success("Done!")
