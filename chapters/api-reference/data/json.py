import streamlit as st

st.title("🔷 st.json()")

st.divider()

st.write('''
- Display an object or string as a pretty-printed, interactive JSON string
''')

st.divider()

code = '''
st.json(
    {
        "foo": "bar",
        "stuff": [
            "stuff 1",
            "stuff 2",
            "stuff 3",
        ],
        "level1": {"level2": {"level3": {"a": "b"}}},
    },
    expanded=2,
)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.json(
    {
        "foo": "bar",
        "stuff": [
            "stuff 1",
            "stuff 2",
            "stuff 3",
        ],
        "level1": {"level2": {"level3": {"a": "b"}}},
    },
    expanded=2,
)
