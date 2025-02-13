import streamlit as st

st.title("🔷 st.form_submit_button()")

st.divider()

st.write('''
- Display a form submit button
- When this button is clicked, all widget values inside the form will be sent from the user's browser to your Streamlit server in a batch
- Every form must have at least one `st.form_submit_button`
- An `st.form_submit_button` cannot exist outside of a form
''')

st.divider()

code = '''
with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
st.write("Outside the form")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
st.write("Outside the form")
