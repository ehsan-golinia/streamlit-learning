import streamlit as st
from datetime import time, datetime

st.title("🔷 st.select_slider()")

st.divider()

st.write('''
- Display a slider widget to select items from a list
- This also allows you to render a range slider by passing a two-element tuple or list as the `value`
- The difference between `st.select_slider` and `st.slider` is that `select_slider` accepts any datatype and takes an iterable set of options,
 while `st.slider` only accepts numerical or date/time data and takes a range as input.
''')

st.divider()

code = '''
color = st.select_slider(
    "Select a color of the rainbow",
    options=[
        "red",
        "orange",
        "green",
        "blue",
        "violet",
    ],
)
st.write(f"My favorite color is :{color}[{color}]")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

color = st.select_slider(
    "Select a color of the rainbow",
    options=[
        "red",
        "orange",
        "green",
        "blue",
        "violet",
    ],
)
st.write(f"My favorite color is :{color}[{color}]")

st.divider()

code = '''
start_color, end_color = st.select_slider(
    "Select a range of color wavelength",
    options=[
        "red",
        "orange",
        "green",
        "blue",
        "violet",
    ],
    value=("red", "blue"),
)
st.write(f"You selected wavelengths between :{start_color}[{start_color}] and :{end_color}[{end_color}]")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

start_color, end_color = st.select_slider(
    "Select a range of color wavelength",
    options=[
        "red",
        "orange",
        "green",
        "blue",
        "violet",
    ],
    value=("red", "blue"),
)
st.write(f"You selected wavelengths between :{start_color}[{start_color}] and :{end_color}[{end_color}]")

st.divider()

code = '''
val = st.select_slider(
    "Select a range of color wavelength",
    options=range(1, 9),
    value=6
)
st.write(f"You chose {val} hearts: {"💚" * val}")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

val = st.select_slider(
    "Select a range of color wavelength",
    options=range(1, 9),
    value=6
)
st.write(f"You chose {val} hearts: {"💚" * val}")
