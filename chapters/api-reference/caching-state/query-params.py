import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from vega_datasets import data

st.title("🔷 st.query_params()")

st.divider()

st.write('''
- `st.query_params` provides a dictionary-like interface to access query parameters in your app's URL and is available as of Streamlit 1.30.0
- It behaves similarly to `st.session_state` with the notable exception that keys may be repeated in an app's URL
- Handling of repeated keys requires special consideration as explained below
- `st.query_params` can be used with both key and attribute notation
''')

st.divider()

code = '''
# https://your_app.streamlit.app/?first_key=1&second_key=two&third_key=true

\"""
{
    "first_key" : "1",
    "second_key" : "two",
    "third_key" : "true"
}
\"""
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

# https://your_app.streamlit.app/?first_key=1&second_key=two&third_key=true

st.write(st.query_params)

st.divider()

code = '''
# You can read query params using key notation
if st.query_params["first_key"] == "1":
    st.write(":violet[The first key is 1]")

# ...or using attribute notation
if st.query_params.second_key == "two":
    st.write(":green[The second key is two]")

# And you can change a param by just writing to it
st.query_params.third_key = 2  # This gets converted to str automatically

st.write(":orange[The third key is now 2]")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

# You can read query params using key notation
if st.query_params["first_key"] == "1":
    st.write(":violet[The first key is 1]")

# ...or using attribute notation
if st.query_params.second_key == "two":
    st.write(":green[The second key is two]")

# And you can change a param by just writing to it
st.query_params.third_key = 2  # This gets converted to str automatically

st.write(":orange[The third key is now 2]")
