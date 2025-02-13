import streamlit as st

st.title("🔷 Example 1")

st.divider()

code = '''
# A simple counter variable, without session state
counter = 0

st.write(f"Counter value = {counter}")

# Button to increment the counter
if st.button("+ Counter +"):
    counter += 1
    st.write(f"Counter value = {counter}")
else:
    st.write(f"Counter value = {counter}")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

# A simple counter variable, without session state
counter = 0

st.write(f"Counter value = {counter}")

# Button to increment the counter
if st.button("+ Counter +"):
    counter += 1
    st.write(f"Counter value = {counter}")
else:
    st.write(f"Counter value = {counter}")

st.divider()

code = '''
if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.write(f"Counter value = {st.session_state.counter}")

if st.button("Reset"):
    st.session_state.counter = 0

st.write(f"Counter value = {st.session_state.counter}")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.write(f"Counter value = {st.session_state.counter}")

if st.button("Reset"):
    st.session_state.counter = 0

st.write(f"Counter value = {st.session_state.counter}")
