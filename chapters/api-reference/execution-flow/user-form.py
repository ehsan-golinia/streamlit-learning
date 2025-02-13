import streamlit as st
from datetime import datetime

MIN_DATE = datetime(1900, 1, 1)
MAX_DATE = datetime.now()

st.title("🔷 User Information Form")

st.divider()

form_values = {
    "name": None,
    "height": None,
    "gender": None,
    "dob": None
}

with st.form(key="user_info_form", clear_on_submit=True):
    form_values["name"] = st.text_input("Enter your name: ")
    form_values["height"] = st.number_input("Enter your height: (cm)", min_value=0)
    form_values["gender"] = st.selectbox("Select your gender: ", ["Male", "Female"])
    form_values["dob"] = st.date_input(
        "Enter your date of birth: ",
        min_value=MIN_DATE,
        max_value=MAX_DATE)

    if form_values["dob"]:
        age = MAX_DATE.year - form_values["dob"].year
        if form_values["dob"].month > MAX_DATE.month or (
                form_values["dob"].month == MAX_DATE.month and form_values["dob"].day > MAX_DATE.day):
            age -= 1
        st.write(f"You are :orange[{age}] years old")

    submit_button = st.form_submit_button("Submit")
    if submit_button:
        if not all(form_values.values()):
            st.warning("Please fill in all the fields")
        else:
            st.balloons()
            st.write("Name: ", form_values["name"])
            st.write("Height: ", form_values["height"], "cm")
            st.write("Gender: ", form_values["gender"])
            st.write("Date of Birth: ", form_values["dob"])
