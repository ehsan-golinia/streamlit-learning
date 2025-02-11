import streamlit as st

introduction = st.Page(
    "chapters/introduction.py", title="Home",
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

markdown = st.Page(
    "chapters/api-reference/text/markdown.py", title="st.markdown",
    icon=":material/dashboard:"
)
title = st.Page(
    "chapters/api-reference/text/title.py", title="st.title",
    icon=":material/dashboard:"
)
header = st.Page(
    "chapters/api-reference/text/header.py", title="st.header",
    icon=":material/dashboard:"
)
subheader = st.Page(
    "chapters/api-reference/text/subheader.py", title="st.subheader",
    icon=":material/dashboard:"
)
caption = st.Page(
    "chapters/api-reference/text/caption.py", title="st.caption",
    icon=":material/dashboard:"
)
code = st.Page(
    "chapters/api-reference/text/code.py", title="st.code",
    icon=":material/dashboard:"
)
latex = st.Page(
    "chapters/api-reference/text/latex.py", title="st.latex",
    icon=":material/dashboard:"
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
radio = st.Page(
    "chapters/api-reference/input-widgets/radio.py", title="st.radio",
    icon=":material/dashboard:"
)
rbc = st.Page(
    "chapters/api-reference/input-widgets/rbc.py", title="radio, button, checkbox",
    icon=":material/dashboard:"
)
selectbox = st.Page(
    "chapters/api-reference/input-widgets/selectbox.py", title="st.selectbox",
    icon=":material/dashboard:"
)
number_input = st.Page(
    "chapters/api-reference/input-widgets/number-input.py", title="st.number_input",
    icon=":material/dashboard:"
)
text_input = st.Page(
    "chapters/api-reference/input-widgets/text-input.py", title="st.text_input",
    icon=":material/dashboard:"
)
link_button = st.Page(
    "chapters/api-reference/input-widgets/link-button.py", title="st.link_button",
    icon=":material/dashboard:"
)
file_uploader = st.Page(
    "chapters/api-reference/input-widgets/file-uploader.py", title="st.file_uploader",
    icon=":material/dashboard:"
)

image = st.Page(
    "chapters/api-reference/media/image.py", title="st.image",
    icon=":material/dashboard:"
)
logo = st.Page(
    "chapters/api-reference/media/logo.py", title="st.logo",
    icon=":material/dashboard:"
)
audio = st.Page(
    "chapters/api-reference/media/audio.py", title="st.audio",
    icon=":material/dashboard:"
)
video = st.Page(
    "chapters/api-reference/media/video.py", title="st.video",
    icon=":material/dashboard:"
)

bar_chart = st.Page(
    "chapters/api-reference/charts/bar-chart.py", title="st.bar_chart",
    icon=":material/dashboard:"
)
line_chart = st.Page(
    "chapters/api-reference/charts/line-chart.py", title="st.line_chart",
    icon=":material/dashboard:"
)

columns = st.Page(
    "chapters/api-reference/layouts/columns.py", title="st.columns",
    icon=":material/dashboard:"
)
empty = st.Page(
    "chapters/api-reference/layouts/empty.py", title="st.empty",
    icon=":material/dashboard:"
)

metric = st.Page(
    "chapters/api-reference/data/metric.py", title="st.metric",
    icon=":material/dashboard:"
)

pg = st.navigation(
    {
        "": [introduction],
        
        "🔶 Start": [install, create, run],

        "🔶 Text": [markdown, title, header, subheader, caption, code, latex],

        "🔶 Write & magic": [write, write_stream, magic],

        "🔶 Input widgets": [
            button, checkbox, radio, rbc, selectbox, number_input, text_input,
            link_button, file_uploader],

        "🔶 Media elements": [image, logo, audio, video],

        "🔶 Chart elements": [bar_chart, line_chart],

        "🔶 Layouts": [columns, empty],

        "🔶 Data elements": [metric],
    },
)

pg.run()
