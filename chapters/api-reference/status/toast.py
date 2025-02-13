import streamlit as st
import time

st.title("🔷 st.toast()")

st.divider()

st.write('''
- Display a short message, known as a notification "toast"
-The toast appears in the app's bottom-right corner and disappears after four seconds
''')

st.divider()

code = '''
st.toast('Your edited image was saved!', icon='😍')
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.toast('Your edited image was saved!', icon='😍')

st.divider()

code = '''
if st.button('Three cheers'):
    st.toast('Hip!')
    time.sleep(2)
    st.toast('Hip!')
    time.sleep(2)
    st.toast('Hooray!', icon='🎉')
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

if st.button('Three cheers'):
    st.toast('Hip!')
    time.sleep(2)
    st.toast('Hip!')
    time.sleep(2)
    st.toast('Hooray!', icon='🎉')

st.divider()

code = '''
def cook_breakfast():
    msg = st.toast('Gathering ingredients...')
    time.sleep(2)
    msg.toast('Cooking...')
    time.sleep(2)
    msg.toast('Ready!', icon="🥞")

if st.button('Cook breakfast'):
    cook_breakfast()
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

def cook_breakfast():
    msg = st.toast('Gathering ingredients...')
    time.sleep(2)
    msg.toast('Cooking...')
    time.sleep(2)
    msg.toast('Ready!', icon="🥞")

if st.button('Cook breakfast'):
    cook_breakfast()
