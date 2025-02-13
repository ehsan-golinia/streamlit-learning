import streamlit as st
import datetime

st.title("🔷 st.time_input()")

st.divider()

st.write('''
- Display a time input widget
''')

st.divider()

code = '''
t = st.time_input("Set an alarm for", datetime.time(8, 45))
st.write("Alarm is set for", t)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

t = st.time_input("Set an alarm for", datetime.time(8, 45))
st.write("Alarm is set for", t)

st.divider()

code = '''
t = st.time_input("Set an alarm for", value=None, step=300)
st.write("Alarm is set for", t)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

t = st.time_input("Set an alarm for", value=None, step=300)
st.write("Alarm is set for", t)