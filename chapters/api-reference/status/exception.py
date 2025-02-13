import streamlit as st

st.title("🔷 st.exception()")

st.divider()

st.write('''
- Display an exception
''')

st.divider()

code = '''
if st.button("Exception"):
    e = RuntimeError("This is an exception of type RuntimeError")
    st.exception(e)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

if st.button("Exception"):
    e = RuntimeError("This is an exception of type RuntimeError")
    st.exception(e)
