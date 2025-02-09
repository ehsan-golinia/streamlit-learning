import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from vega_datasets import data

st.title("🔷 st.columns()")

st.divider()

st.write('''
- Insert containers laid out as side-by-side columns
''')

st.divider()

code = '''col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

st.divider()

code = '''col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)

st.divider()

code = '''left, middle, right = st.columns(3, vertical_alignment="bottom")

left.text_input("Write something")
middle.button("Click me", use_container_width=True)
right.checkbox("Check me")'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

left, middle, right = st.columns(3, vertical_alignment="bottom")

left.text_input("Write something")
middle.button("Click me", use_container_width=True)
right.checkbox("Check me")

st.divider()

code = '''vertical_alignment = st.selectbox(
    "Vertical alignment", ["top", "center", "bottom"], index=2
)

left, middle, right = st.columns(3, vertical_alignment=vertical_alignment)
left.image("https://static.streamlit.io/examples/cat.jpg")
middle.image("https://static.streamlit.io/examples/dog.jpg")
right.image("https://static.streamlit.io/examples/owl.jpg")'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

vertical_alignment = st.selectbox(
    "Vertical alignment", ["top", "center", "bottom"], index=2
)

left, middle, right = st.columns(3, vertical_alignment=vertical_alignment)
left.image("https://static.streamlit.io/examples/cat.jpg")
middle.image("https://static.streamlit.io/examples/dog.jpg")
right.image("https://static.streamlit.io/examples/owl.jpg")

st.divider()

code = '''left, middle, right = st.columns(3, border=True)

left.markdown("Lorem ipsum " * 10)
middle.markdown("Lorem ipsum " * 5)
right.markdown("Lorem ipsum ")'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

left, middle, right = st.columns(3, border=True)

left.markdown("Lorem ipsum " * 10)
middle.markdown("Lorem ipsum " * 5)
right.markdown("Lorem ipsum ")
