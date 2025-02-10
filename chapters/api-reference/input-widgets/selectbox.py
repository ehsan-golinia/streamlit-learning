import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

st.title("🔷 st.selectbox()")

st.divider()

st.write('''
- Display a select widget''')

st.divider()

code = '''
option1 = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write(":blue[You selected:]", option1)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

option1 = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write(":blue[You selected:]", option1)

st.divider()

code = '''
option2 = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
    index=None,
    placeholder="Select contact method...",
)

st.write(":blue[You selected:]", option2)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

option2 = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
    index=None,
    placeholder="Select contact method...",
)

st.write(":blue[You selected:]", option2)

st.divider()

code = '''
# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option3 = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option3 = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone", "Fax"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )
