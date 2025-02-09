import time
import streamlit as st
import pandas as pd
import numpy as np

st.title("🔷 st.write_stream()")

st.divider()

st.write('''
- Stream a generator, iterable, or stream-like sequence to the app
- `st.write_stream` iterates through the given sequences and writes all chunks to the app
- String chunks will be written using a typewriter effect''')

st.divider()

code = '''_LOREM_IPSUM = \"""
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
\"""


def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.2)

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.2)


if st.button("Stream data"):
    st.write_stream(stream_data)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

_LOREM_IPSUM = """
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""


def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.2)

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.2)


if st.button("Stream data"):
    st.write_stream(stream_data)

