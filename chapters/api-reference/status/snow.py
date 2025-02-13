import streamlit as st

st.title("🔷 st.snow()")

st.divider()

st.write('''
- Draw celebratory snowfall
''')

st.divider()

code = '''
if st.button("Balloons"):
    st.snow()
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

if st.button("Balloons"):
    st.snow()
