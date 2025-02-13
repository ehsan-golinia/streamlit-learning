import streamlit as st
import time

st.title("🔷 st.spinner()")

st.divider()

st.write('''
- Display a loading spinner while executing a block of code
''')

st.divider()

code = '''
with st.spinner("Wait for it...", show_time=True):
    time.sleep(5)
st.success("Done!")
st.button("Rerun")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

with st.spinner("Wait for it...", show_time=True):
    time.sleep(5)
st.success("Done!")
st.button("Rerun")
