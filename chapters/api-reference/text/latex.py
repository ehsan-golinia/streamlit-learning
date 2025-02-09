import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from vega_datasets import data

st.title("🔷 st.latex()")

st.divider()

st.write('''
- Display mathematical expressions formatted as LaTeX
- Supported LaTeX functions are listed at https://katex.org/docs/supported.html
''')

st.divider()

code = '''
st.latex(r\'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    \''')'''
st.code(code, language="python")

st.markdown(":orange[Output:]")


st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
