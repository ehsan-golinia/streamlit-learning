import streamlit as st
import time

st.title("🔷 st.status()")

st.divider()

st.write('''
- Insert a status container to display output from long-running tasks
- Inserts a container into your app that is typically used to show the status and details of a process or task
- The container can hold multiple elements and can be expanded or collapsed by the user similar to `st.expander`
- When collapsed, all that is visible is the status icon and label
''')

st.divider()

code = '''
with st.status("Downloading data..."):
    st.write("Searching for data...")
    time.sleep(10)
    st.write("Found URL.")
    time.sleep(10)
    st.write("Downloading data...")
    time.sleep(10)

st.button("Rerun")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

with st.status("Downloading data..."):
    st.write("Searching for data...")
    time.sleep(10)
    st.write("Found URL.")
    time.sleep(10)
    st.write("Downloading data...")
    time.sleep(10)

st.button("Rerun")

st.divider()

code = '''
with st.status("Downloading data...", expanded=True) as status:
    st.write("Searching for data...")
    time.sleep(10)
    st.write("Found URL.")
    time.sleep(10)
    st.write("Downloading data...")
    time.sleep(10)
    status.update(
        label="Download complete!", state="complete", expanded=False
    )

st.button("Run again")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")


with st.status("Downloading data...", expanded=True) as status:
    st.write("Searching for data...")
    time.sleep(10)
    st.write("Found URL.")
    time.sleep(10)
    st.write("Downloading data...")
    time.sleep(10)
    status.update(
        label="Download complete!", state="complete", expanded=False
    )

st.button("Run again")
