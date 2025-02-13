import streamlit as st

st.title("🔷 st.warning()")

st.divider()

st.write('''
- Display warning message
''')

st.divider()

code = '''
if st.button("Warning"):
    st.warning('This is a warning', icon="⚠️")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

if st.button("Warning"):
    st.warning('This is a warning', icon="⚠️")
