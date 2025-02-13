import streamlit as st
import time

st.title("🔷 st.dialog()")

st.divider()

st.write('''
- Function decorator to create a modal dialog
- A function decorated with `@st.dialog` becomes a dialog function
- When you call a dialog function, Streamlit inserts a modal dialog into your app
- Streamlit element commands called within the dialog function render inside the modal dialog
- The dialog function can accept arguments that can be passed when it is called
- Any values from the dialog that need to be accessed from the wider app should generally be stored in Session State
''')

st.divider()

code = '''
@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"
