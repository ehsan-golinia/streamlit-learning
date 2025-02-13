import streamlit as st

st.title("🔷 st.balloons()")

st.divider()

st.write('''
- Draw celebratory balloons
''')

st.divider()

code = '''
if st.button("Balloons"):
    st.balloons()
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

if st.button("Balloons"):
    st.balloons()
