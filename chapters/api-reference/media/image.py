import streamlit as st
import os

st.title("🔷 st.image()")

st.divider()

st.write('''
- Display an image or list of images
''')

st.divider()

code = '''
st.image(
    "chapters/api-reference/media/sunrise.jpeg",
    caption="Sunrise by the mountains",
    width=200)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.image(
    "chapters/api-reference/media/sunrise.jpeg",
    caption="Sunrise by the mountains",
    width=200)

st.divider()

code = '''
st.image(
    os.path.join(os.getcwd(), "chapters/api-reference/media/sunrise.jpeg"), 
    caption="Sunrise by the mountains")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.image(
    os.path.join(os.getcwd(), "chapters/api-reference/media/sunrise.jpeg"),
    caption="Sunrise by the mountains")
