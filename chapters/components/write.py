import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("🔷 st.write()")

st.divider()

code = '''st.write("Hello, *World!* :sunglasses:")'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.write("Hello, *World!* :sunglasses:")

st.divider()

code = '''st.write(1234)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.write(1234)

st.divider()

code = '''st.write(
    pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )
)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.write(
    pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )
)

st.divider()

code = '''st.write("1 + 1 = ", 2)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.write("1 + 1 = ", 2)

st.divider()

code = '''data_frame = pd.DataFrame(
    {
        "first column": [1, 2, 3, 4],
        "second column": [10, 20, 30, 40],
    }
)

st.write("Below is a DataFrame:", data_frame, "Above is a dataframe.")'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

data_frame = pd.DataFrame(
    {
        "first column": [1, 2, 3, 4],
        "second column": [10, 20, 30, 40],
    }
)

st.write("Below is a DataFrame:", data_frame, "Above is a dataframe.")

st.divider()

code = '''df = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])

c = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.write(c)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

df = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])

c = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.write(c)
