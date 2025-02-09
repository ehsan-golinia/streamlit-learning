import streamlit as st

st.title("🔷 Run")

st.divider()

st.write('Run `app.py` file')

code = '''streamlit run app.py'''
st.code(code, language=None)
