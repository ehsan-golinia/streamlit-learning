import streamlit as st
import time

st.title("🔷 st.sidebar()")

st.divider()

st.write('''
- Not only can you add interactivity to your app with widgets, you can organize them into a sidebar
- Elements can be passed to st.sidebar using object notation and with notation
''')

st.divider()

code = '''
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

st.divider()

code = '''
with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")
