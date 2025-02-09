import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

st.title("🔷 Magic")

st.divider()

st.write('''
- Write common data science objects
    - Markdown
    - Numbers
    - DataFrames
    - Charts
- Simply use variables or literal values''')

st.divider()

code = ''' \'''
# This is the document title

This is some __markdown__.
\''' '''
st.code(code, language="python")

st.markdown(":orange[Output:]")

'''
# This is the document title

This is some __markdown__.
'''

st.divider()

code = '''import pandas as pd

df = pd.DataFrame({'col1': [1,2,3]})

df'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

df = pd.DataFrame({'col1': [1,2,3]})

df

st.divider()

code = '''x = 10

'x', x'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

x = 10
'x', x

st.divider()

code = '''import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig

st.divider()

st.write('''
If you prefer to call Streamlit commands more explicitly, you can always turn magic off 
in your `~/.streamlit/config.toml` with the following setting:''')

code = '''[runner]
magicEnabled = false
'''
st.code(code, language=None)
