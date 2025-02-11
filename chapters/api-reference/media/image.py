import streamlit as st

st.title("🔷 st.image()")

st.divider()

st.write('''
- Display an image or list of images
''')

st.divider()

code = '''st.image("sunrise.jpg", caption="Sunrise by the mountains")'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.image("chapters/api-reference/media/sunrise.jpeg", caption="Sunrise by the mountains")
