import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

st.title("🔷 st.write()")

st.divider()

st.write('''
- Write arguments to the Streamlit app
- Accepts multiple arguments
- Supports various data types
    - string
    - pandas data frames
    - array
    - list, tuple, dictionaries
    - ML model
    - matplotlib charts
    - plotly figures
    - Altair
    - Object''')

st.divider()

code = '''st.write("Hello, *World!* :sunglasses:")'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.write("Hello, *World!* :sunglasses:")

st.divider()

code = '''st.write(\'''
# This is the document title

This is some __markdown__.
\''')'''
st.code(code, language=None)

st.markdown(":orange[Output:]")

st.write('''
# This is the document title

This is some __markdown__.
''')

st.divider()

code = '''st.write(1234)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.write(1234)

st.divider()

code = '''st.write({"key": ["val1", "val2", "val3"]})'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.write({"key": ["val1", "val2", "val3"]})

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

st.divider()

code = '''import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.write(fig)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.write(fig)

st.divider()

code = '''
st.write(np.array([1, 2, 3, 4]))
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.write(np.array([1, 2, 3, 4]))
