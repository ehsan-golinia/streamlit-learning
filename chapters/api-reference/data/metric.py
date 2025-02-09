import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from vega_datasets import data

st.title("🔷 st.metric()")

st.divider()

st.write('''
- Display a metric in big bold font, with an optional indicator of how the metric changed
''')

st.divider()

code = '''st.metric(label="Temperature", value="70 °F", delta="1.2 °F")'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

st.divider()

code = '''col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.divider()

code = '''st.metric(label="Gas price", value=4, delta=-0.5, delta_color="inverse")

st.metric(
    label="Active developers", value=123, delta=123, delta_color="off"
)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.metric(label="Gas price", value=4, delta=-0.5, delta_color="inverse")

st.metric(
    label="Active developers", value=123, delta=123, delta_color="off"
)

st.divider()

code = '''a, b = st.columns(2)
c, d = st.columns(2)

a.metric("Temperature", "30°F", "-9°F", border=True)
b.metric("Wind", "4 mph", "2 mph", border=True)

c.metric("Humidity", "77%", "5%", border=True)
d.metric("Pressure", "30.34 inHg", "-2 inHg", border=True)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

a, b = st.columns(2)
c, d = st.columns(2)

a.metric("Temperature", "30°F", "-9°F", border=True)
b.metric("Wind", "4 mph", "2 mph", border=True)

c.metric("Humidity", "77%", "5%", border=True)
d.metric("Pressure", "30.34 inHg", "-2 inHg", border=True)
