import streamlit as st
import time

st.title("🔷 st.expander()")

st.divider()

st.write('''
- Inserts a container into your app that can be used to hold multiple elements and can be expanded or collapsed by the user
- When collapsed, all that is visible is the provided label
- To add elements to the returned container, you can use the `with` notation (preferred)''')

st.divider()

code = '''
st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write(\'''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    \''')
    st.image("https://static.streamlit.io/examples/dice.jpg")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')
    st.image("https://static.streamlit.io/examples/dice.jpg")

st.divider()

code = '''
st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

expander = st.expander("See explanation")
expander.write(\'''
    The chart above shows some numbers I picked for you.
    I rolled actual dice for these, so they're *guaranteed* to
    be random.
\''')
expander.image("https://static.streamlit.io/examples/dice.jpg")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

expander = st.expander("See explanation")
expander.write('''
    The chart above shows some numbers I picked for you.
    I rolled actual dice for these, so they're *guaranteed* to
    be random.
''')
expander.image("https://static.streamlit.io/examples/dice.jpg")
