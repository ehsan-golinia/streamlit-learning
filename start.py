import streamlit as st

# st.page_link("introduction.py", label="Home", icon="🏠")

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
    "chapters/components/write.py", title="st.write", 
    icon=":material/dashboard:"
)

pg = st.navigation(
    {
        "": [introduction],
        
        "🔶 Start": [install, create, run],
        
        "🔶 Components": [write],
    },
)

pg.run()
