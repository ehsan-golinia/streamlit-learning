import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

st.title("🔷 RBC")

st.divider()

st.write('''
- Radio button
- Checkbox
- Button''')

st.divider()

code = '''
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

page_names = ["Checkbox", "Button"]

page = st.radio("Navigation", page_names)

if page == "Checkbox":
    st.session_state.clicked = False
    st.subheader("Welcome to the Checkbox page!")
    st.write("Nice to see you! :wave:")
    check = st.checkbox("Click me!")
    st.write('Checkbox = ', check)
    if check:
        nested_btn = st.button("Button nested in Checkbox")
        if nested_btn:
            st.write(":smile:" * 6)
else:
    st.subheader("Welcome to the Button page!")
    st.write(":thumbsup:")
    result = st.button("Click me!", on_click=click_button)
    st.write('Button = ', result)
    if st.session_state.clicked:
        nested_check = st.checkbox("Checkbox nested in Button")
        if nested_check:
            st.write(":cake:" * 6)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False


def click_button():
    st.session_state.clicked = True


page_names = ["Checkbox", "Button"]

page = st.radio("Navigation", page_names)

if page == "Checkbox":
    st.session_state.clicked = False
    st.subheader("Welcome to the Checkbox page!")
    st.write("Nice to see you! :wave:")
    check = st.checkbox("Click me!")
    st.write('Checkbox = ', check)
    if check:
        nested_btn = st.button("Button nested in Checkbox")
        if nested_btn:
            st.write(":smile:" * 6)
else:
    st.subheader("Welcome to the Button page!")
    st.write(":thumbsup:")
    result = st.button("Click me!", on_click=click_button)
    st.write('Button = ', result)
    if st.session_state.clicked:
        nested_check = st.checkbox("Checkbox nested in Button")
        if nested_check:
            st.write(":cake:" * 6)
