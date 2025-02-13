import streamlit as st

st.title("🔷 st.form()")

st.divider()

st.write('''
- Create a form that batches elements together with a "Submit" button
- A form is a container that visually groups other elements and widgets together, and contains a Submit button
- When the form's Submit button is pressed, all widget values inside the form will be sent to Streamlit in a batch
- To add elements to a form object, you can use `with` notation
''')

st.divider()

code = '''
with st.form(key="my_form"):
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

with st.form(key="my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
st.write("Outside the form")

st.divider()

code = '''
form = st.form("my_form_2")
form.slider("Inside the form")
st.slider("Outside the form")

# Now add a submit button to the form:
form.form_submit_button("Submit")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

form = st.form("my_form_2")
form.slider("Inside the form")
st.slider("Outside the form")

# Now add a submit button to the form:
form.form_submit_button("Submit")

st.divider()

code = '''
with st.form(key="sample_form"):
    # Text Input
    st.subheader("Text Inputs")
    name = st.text_input("Enter your name")
    feedback = st.text_area("Provide your feedback")

    # Date and Time Inputs
    st.subheader("Date and Time Inputs")
    dob = st.date_input("Select your date of birth")
    this_time = st.time_input("Choose a preferred time")

    # Selectors
    st.subheader("Selectors")
    choice = st.radio("Choose an option", ['Option 1', 'Option 2', 'Option 3'])
    gender = st.selectbox("Select your gender", ['Male', 'Female'])
    slider_value = st.select_slider("Select a range", options=[1, 2, 3, 4, 5, 6])

    # Toggles and Checkboxes
    st.subheader("Toggles and Checkboxes")
    notifications = st.checkbox("Receive notifications?")
    toggle_value = st.checkbox("Enable dark mode?", value=False)

    submit_button = st.form_submit_button(label="Submit")

st.subheader("Info")
if submit_button:
    st.write(f"Hello, {name}")
    st.success("Your feedback has been successfully submitted")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

with st.form(key="sample_form"):
    # Text Input
    st.subheader("Text Inputs")
    name = st.text_input("Enter your name")
    feedback = st.text_area("Provide your feedback")

    # Date and Time Inputs
    st.subheader("Date and Time Inputs")
    dob = st.date_input("Select your date of birth")
    this_time = st.time_input("Choose a preferred time")

    # Selectors
    st.subheader("Selectors")
    choice = st.radio("Choose an option", ['Option 1', 'Option 2', 'Option 3'])
    gender = st.selectbox("Select your gender", ['Male', 'Female'])
    slider_value = st.select_slider("Select a range", options=[1, 2, 3, 4, 5, 6])

    # Toggles and Checkboxes
    st.subheader("Toggles and Checkboxes")
    notifications = st.checkbox("Receive notifications?")
    toggle_value = st.checkbox("Enable dark mode?", value=False)

    submit_button = st.form_submit_button(label="Submit")

st.subheader("Info")
if submit_button:
    st.write(f"Hello, {name}")
    st.success("Your feedback has been successfully submitted")
