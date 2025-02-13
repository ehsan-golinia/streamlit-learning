import streamlit as st

st.title("🔷 st.info()")

st.divider()

st.write('''
- Display an informational message
''')

st.divider()

code = '''
if st.button("Info"):
    st.info('This is a purely informational message', icon="ℹ️")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

if st.button("Info"):
    st.info('This is a purely informational message', icon="ℹ️")
