import streamlit as st

st.title("🔷 st.popover()")

st.divider()

st.write('''
- Insert a popover container
- Inserts a multi-element container as a popover
- It consists of a button-like element and a container that opens when the button is clicked
- Opening and closing the popover will not trigger a rerun
- Interacting with widgets inside of an open popover will rerun the app while keeping the popover open
- Clicking outside of the popover will close it
''')

st.divider()

code = '''
with st.popover("Open popover"):
    st.markdown("Hello World 👋")
    name = st.text_input("What's your name?")

st.write("Your name:", name)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

with st.popover("Open popover"):
    st.markdown("Hello World 👋")
    name = st.text_input("What's your name?")

st.write("Your name:", name)

st.divider()

code = '''
popover = st.popover("Filter items")
red = popover.checkbox("Show red items.", True)
blue = popover.checkbox("Show blue items.", True)

if red:
    st.write(":red[This is a red item.]")
if blue:
    st.write(":blue[This is a blue item.]")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

popover = st.popover("Filter items")
red = popover.checkbox("Show red items.", True)
blue = popover.checkbox("Show blue items.", True)

if red:
    st.write(":red[This is a red item.]")
if blue:
    st.write(":blue[This is a blue item.]")
