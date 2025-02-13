import streamlit as st

st.title("🔷 st.success()")

st.divider()

st.write('''
- Display a success message
''')

st.divider()

code = '''
if st.button("Success"):
    st.success('This is a success message!', icon="✅")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

if st.button("Success"):
    st.success('This is a success message!', icon="✅")
