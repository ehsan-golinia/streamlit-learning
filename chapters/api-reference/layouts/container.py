import streamlit as st
import numpy as np

st.title("🔷 st.container()")

st.divider()

st.write('''
- Insert a multi-element container
- Inserts an invisible container into your app that can be used to hold multiple elements
- This allows you to, for example, insert multiple elements into your app out of order
- To add elements to the returned container, you can use the `with` notation (preferred)
''')

st.divider()

code = '''
with st.container():
    st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

with st.container():
    st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")

st.divider()

code = '''
container = st.container(border=True)
container.write("This is inside the container")
st.write("This is outside the container")

# Now insert some more in the container
container.write("This is inside too")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

container = st.container(border=True)
container.write("This is inside the container")
st.write("This is outside the container")

# Now insert some more in the container
container.write("This is inside too")

st.divider()

code = '''
row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
    tile = col.container(height=120)
    tile.title(":balloon:")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
    tile = col.container(height=120)
    tile.title(":balloon:")

st.divider()

code = '''
long_text = "Lorem ipsum. " * 1000

with st.container(height=300):
    st.markdown(long_text)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

long_text = "Lorem ipsum. " * 1000

with st.container(height=300):
    st.markdown(long_text)
