import streamlit as st

st.title("🔷 st.divider()")

st.divider()

st.write('''
- Display a horizontal rule
''')

st.divider()

code = '''
st.write("This is some text.")

st.slider("This is a slider", 0, 100, (25, 75))

st.divider()  # 👈 Draws a horizontal rule

st.write("This text is between the horizontal rules.")

st.divider()  # 👈 Another horizontal rule
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.write("This is some text.")

st.slider("This is a slider", 0, 100, (25, 75))

st.divider()  # 👈 Draws a horizontal rule

st.write("This text is between the horizontal rules.")

st.divider()  # 👈 Another horizontal rule
