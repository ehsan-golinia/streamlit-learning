import streamlit as st

st.title("🔷 st.error()")

st.divider()

st.write('''
- Display error message
''')

st.divider()

code = '''
if st.button("Error"):
    st.error('This is an error', icon="🚨")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

if st.button("Error"):
    st.error('This is an error', icon="🚨")
