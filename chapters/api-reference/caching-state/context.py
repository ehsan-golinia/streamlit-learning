import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from vega_datasets import data

st.title("🔷 st.context()")

st.divider()

st.write('''
- An interface to access user session context
- `st.context` provides a read-only interface to access headers and cookies for the current user session
- Each property (`st.context.headers` and `st.context.cookies`) returns a dictionary of named values
''')

st.divider()

code = '''
st.write(st.context.cookies)

st.write(st.context.cookies["sessionid"])
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.write(st.context.cookies)

st.write(st.context.cookies["sessionid"])

st.divider()

code = '''
st.write(st.context.headers)

st.write(st.context.headers["host"])

st.write(st.context.headers.get_all("pragma"))
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.write(st.context.headers)

st.write(st.context.headers["host"])

st.write(st.context.headers.get_all("pragma"))
