import streamlit as st

st.title("🔷 st.session_state()")

st.divider()

st.write('''
- Session State is a way to share variables between reruns, for each user session
- In addition to the ability to store and persist state, Streamlit also exposes the ability to manipulate state using Callbacks
- Session state also persists across apps inside a multipage app
''')

st.divider()

code = '''
# Initialization
if 'key' not in st.session_state:
    st.session_state['key'] = 'value1234'

# Session State also supports attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value1234'

st.write(st.session_state['key'])
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

# Initialization
if 'key' not in st.session_state:
    st.session_state['key'] = 'value1234'

# Session State also supports attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value1234'

st.write(st.session_state['key'])

st.divider()

code = '''
st.session_state.key = 'value2'     # Attribute API
st.session_state['key'] = 'value2'  # Dictionary like API

st.write(st.session_state['key'])
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.session_state.key = 'value2'     # Attribute API
st.session_state['key'] = 'value2'  # Dictionary like API

st.write(st.session_state['key'])

st.divider()

code = '''
# Delete a single key-value pair
del st.session_state['key']

if 'key' not in st.session_state:
    st.write("There is no key in session state")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

# Delete a single key-value pair
del st.session_state['key']

if 'key' not in st.session_state:
    st.write("There is no key in session state")

st.divider()

code = '''
st.text_input("Your name", key="name")

# This exists now:
st.write(st.session_state.name)

# Delete all the items in Session state
for key in st.session_state.keys():
    del st.session_state[key]

if 'key' not in st.session_state:
    st.write("There is no key in session state")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.text_input("Your name", key="name")

# This exists now:
st.write(st.session_state.name)

# Delete all the items in Session state
for key in st.session_state.keys():
    del st.session_state[key]

if 'key' not in st.session_state:
    st.write("There is no key in session state")

st.divider()

code = '''
def form_callback():
    out1.write(st.session_state.my_slider)
    out2.write(st.session_state.my_checkbox)

with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)

out1, out2 = st.columns(2)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

def form_callback():
    out1.write(st.session_state.my_slider)
    out2.write(st.session_state.my_checkbox)

with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)

out1, out2 = st.columns(2)
