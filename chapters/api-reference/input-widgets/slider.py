import streamlit as st
from datetime import time, datetime

st.title("🔷 st.slider()")

st.divider()

st.write('''
- Display a slider widget
- This supports int, float, date, time, and datetime types
- This also allows you to render a range slider by passing a two-element tuple or list as the `value`
''')

st.divider()

code = '''
age = st.slider("How old are you?", min_value=0, max_value=130, value=25, step=1)
st.write("I'm ", age, "years old")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

age = st.slider("How old are you?", min_value=0, max_value=130, value=25, step=1)
st.write("I'm ", age, "years old")

st.divider()

code = '''
values = st.slider(
    "Select a range of values", 
    min_value=0.0, 
    max_value=100.0, 
    value=(25.0, 75.0))
st.info(f"Silder range has type: {type(values)}")
st.write("Values:", values)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

values = st.slider(
    "Select a range of values",
    min_value=0.0,
    max_value=100.0,
    value=(25.0, 75.0))
st.info(f"Silder range has type: {type(values)}")
st.write("Values:", values)

st.divider()

code = '''
appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)),
    format="hh:mm",
)
st.write(f"You're scheduled for: :green[{appointment[0].strftime("%H:%M")} - {appointment[1].strftime("%H:%M")}]")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)),
    format="HH:mm",
)
st.write(f"You're scheduled for: :green[{appointment[0].strftime("%H:%M")} - {appointment[1].strftime("%H:%M")}]")

code = '''
start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm",
)
st.write("Start time:", start_time)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm",
)
st.write("Start time:", start_time)
