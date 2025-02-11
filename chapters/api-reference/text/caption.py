import streamlit as st

st.title("🔷 st.caption()")

st.divider()

st.write('''
- Display text in small font
- This should be used for captions, asides, footnotes, sidenotes, and other explanatory text
''')

st.divider()

code = '''
st.caption("This is a string that explains something above.")
st.caption("A caption with _italics_ :blue[colors] and emojis :sunglasses:")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.caption("This is a string that explains something above.")
st.caption("A caption with _italics_ :blue[colors] and emojis :sunglasses:")
