import streamlit as st

st.title("🔷 st.logo()")

st.divider()

st.write('''
- Renders a logo in the upper-left corner of your app and its sidebar
''')

st.divider()

code = '''
ST_LOGO = "chapters/api-reference/media/logo.svg"
HORIZONTAL_RED = "chapters/api-reference/media/horizontal_red.png"
ICON_RED = "chapters/api-reference/media/icon_red.png"
HORIZONTAL_BLUE = "chapters/api-reference/media/horizontal_blue.png"
ICON_BLUE = "chapters/api-reference/media/icon_blue.png"

options = [ST_LOGO, HORIZONTAL_RED, ICON_RED, HORIZONTAL_BLUE, ICON_BLUE]
sidebar_logo = st.selectbox("Sidebar logo", options, 0)
main_body_logo = st.selectbox("Main body logo", options, 0)

st.logo(sidebar_logo, icon_image=main_body_logo)
st.sidebar.markdown("Hi!")'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

ST_LOGO = "chapters/api-reference/media/logo.svg"
HORIZONTAL_RED = "chapters/api-reference/media/horizontal_red.png"
ICON_RED = "chapters/api-reference/media/icon_red.png"
HORIZONTAL_BLUE = "chapters/api-reference/media/horizontal_blue.png"
ICON_BLUE = "chapters/api-reference/media/icon_blue.png"

options = [ST_LOGO, HORIZONTAL_RED, ICON_RED, HORIZONTAL_BLUE, ICON_BLUE]
sidebar_logo = st.selectbox("Sidebar logo", options, 0)
main_body_logo = st.selectbox("Main body logo", options, 0)

st.logo(
    sidebar_logo,
    link="https://docs.streamlit.io",
    icon_image=main_body_logo)
