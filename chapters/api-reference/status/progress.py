import streamlit as st
import time

st.title("🔷 st.progress()")

st.divider()

st.write('''
- Display a progress bar
''')

st.divider()

code = '''
my_bar = st.empty()
progress_text = "Operation in progress. Please wait."
my_bar.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)

my_bar.button("Rerun")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

my_bar = st.empty()
progress_text = "Operation in progress. Please wait."
my_bar.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)

my_bar.button("Rerun")
