import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from vega_datasets import data

st.title("🔷 st.markdown()")

st.divider()

st.write('''
- Display string formatted as Markdown
''')

st.divider()

code = '''st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown(\'''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.\''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = \'''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
\'''
st.markdown(multi)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

st.divider()

code = '''md = st.text_area('Type in your markdown string (without outer quotes)',
                  "Happy Streamlit-ing! :balloon:")

st.code(f\"""
import streamlit as st

st.markdown(\'''{md}\''')
\""")

st.markdown(md)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

md = st.text_area('Type in your markdown string (without outer quotes)',
                  "Happy Streamlit-ing! :balloon:")

st.code(f"""
import streamlit as st

st.markdown('''{md}''')
""")

st.markdown(md)
