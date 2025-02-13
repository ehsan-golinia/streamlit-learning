import streamlit as st
import datetime

st.title("🔷 st.date_input()")

st.divider()

st.write('''
- Display a date input widget
- The first day of the week is determined from the user's locale in their browser
''')

st.divider()

code = '''
d = st.date_input("When's your birthday", value=datetime.date(2019, 7, 6))
st.write("Your birthday is:", d)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

d = st.date_input("When's your birthday", value=datetime.date(2019, 7, 6))
st.write("Your birthday is:", d)

st.divider()

code = '''
today = datetime.datetime.now()
next_year = today.year + 1
jan_1 = datetime.date(next_year, 1, 1)
dec_31 = datetime.date(next_year, 12, 31)

d = st.date_input(
    "Select your vacation for next year",
    value=(jan_1, datetime.date(next_year, 1, 7)),
    min_value=jan_1,
    max_value=dec_31,
    format="MM.DD.YYYY",
)
st.write(f"From: :green[{d[0]}] To: :green[{d[1]}]")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

today = datetime.datetime.now()
next_year = today.year + 1
jan_1 = datetime.date(next_year, 1, 1)
dec_31 = datetime.date(next_year, 12, 31)

d = st.date_input(
    "Select your vacation for next year",
    value=(jan_1, datetime.date(next_year, 1, 7)),
    min_value=jan_1,
    max_value=dec_31,
    format="MM.DD.YYYY",
)
st.write(f"From: :green[{d[0]}] To: :green[{d[1]}]")

st.divider()

code = '''
d = st.date_input(
    "When's your birthday",
    value=None,
    min_value=datetime.date(1980, 1, 1),
    max_value=datetime.datetime.now().date(),
    format="MM.DD.YYYY",
)
st.write("Your birthday is:", d)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

d = st.date_input(
    "When's your birthday",
    value=None,
    min_value=datetime.date(1980, 1, 1),
    max_value=datetime.datetime.now().date(),
    format="MM.DD.YYYY",
)
st.write("Your birthday is:", d)