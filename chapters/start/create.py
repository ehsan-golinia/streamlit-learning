import streamlit as st

st.title("🔷 Create")

st.divider()

st.write('Create `.py` file')

code = '''touch app.py'''
st.code(code, language=None)

st.write('Then write this simple text')

code = '''import streamlit as st

st.write("Hello World")'''
st.code(code, language="python")

st.markdown(":orange[Output:]")
st.write("Hello World")