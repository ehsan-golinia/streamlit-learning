import streamlit as st

introduction = st.Page(
    "chapters/introduction.py", title="Streamlit", 
    icon="🏠", default=True
)

install = st.Page(
    "chapters/start/install.py", title="Install", 
    icon=":material/install_desktop:"
)
create = st.Page(
    "chapters/start/create.py", title="Create", 
    icon=":material/new_window:"
)
run = st.Page(
    "chapters/start/run.py", title="Run", 
    icon=":material/smart_display:"
)

write = st.Page(
    "chapters/api-reference/write-magic/write.py", title="st.write",
    icon=":material/dashboard:"
)
write_stream = st.Page(
    "chapters/api-reference/write-magic/write_stream.py", title="st.write_stream",
    icon=":material/dashboard:"
)
magic = st.Page(
    "chapters/api-reference/write-magic/magic.py", title="magic commands",
    icon=":material/dashboard:"
)

button = st.Page(
    "chapters/api-reference/input-widgets/button.py", title="st.button",
    icon=":material/dashboard:"
)
checkbox = st.Page(
    "chapters/api-reference/input-widgets/checkbox.py", title="st.checkbox",
    icon=":material/dashboard:"
)

pg = st.navigation(
    {
        "": [introduction],
        
        "🔶 Start": [install, create, run],
        
        "🔶 Write & magic": [write, write_stream, magic],

        "🔶 Input widgets": [button, checkbox],
    },
)

pg.run()
