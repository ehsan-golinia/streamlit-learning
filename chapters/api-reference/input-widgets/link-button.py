import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

st.title("🔷 st.link_button()")

st.divider()

st.write('''
- Display a link button element
- When clicked, a new tab will be opened to the specified URL''')

st.divider()

code = '''st.link_button("Go to gallery", "https://streamlit.io/gallery")'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.link_button("Go to gallery", "https://streamlit.io/gallery")

