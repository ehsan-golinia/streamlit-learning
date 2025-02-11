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

st_markdown = st.Page(
    "chapters/api-reference/text/markdown.py", title="st.markdown",
    icon=":material/dashboard:"
)
st_title = st.Page(
    "chapters/api-reference/text/title.py", title="st.title",
    icon=":material/dashboard:"
)
st_header = st.Page(
    "chapters/api-reference/text/header.py", title="st.header",
    icon=":material/dashboard:"
)
st_subheader = st.Page(
    "chapters/api-reference/text/subheader.py", title="st.subheader",
    icon=":material/dashboard:"
)
st_caption = st.Page(
    "chapters/api-reference/text/caption.py", title="st.caption",
    icon=":material/dashboard:"
)
st_code = st.Page(
    "chapters/api-reference/text/code.py", title="st.code",
    icon=":material/dashboard:"
)
st_latex = st.Page(
    "chapters/api-reference/text/latex.py", title="st.latex",
    icon=":material/dashboard:"
)
st_divider = st.Page(
    "chapters/api-reference/text/divider.py", title="st.divider",
    icon=":material/dashboard:"
)

st_write = st.Page(
    "chapters/api-reference/write-magic/write.py", title="st.write",
    icon=":material/dashboard:"
)
st_write_stream = st.Page(
    "chapters/api-reference/write-magic/write_stream.py", title="st.write_stream",
    icon=":material/dashboard:"
)
st_magic = st.Page(
    "chapters/api-reference/write-magic/magic.py", title="magic commands",
    icon=":material/dashboard:"
)

st_button = st.Page(
    "chapters/api-reference/input-widgets/button.py", title="st.button",
    icon=":material/dashboard:"
)
st_checkbox = st.Page(
    "chapters/api-reference/input-widgets/checkbox.py", title="st.checkbox",
    icon=":material/dashboard:"
)
st_radio = st.Page(
    "chapters/api-reference/input-widgets/radio.py", title="st.radio",
    icon=":material/dashboard:"
)
st_rbc = st.Page(
    "chapters/api-reference/input-widgets/rbc.py", title="radio, button, checkbox",
    icon=":material/dashboard:"
)
st_selectbox = st.Page(
    "chapters/api-reference/input-widgets/selectbox.py", title="st.selectbox",
    icon=":material/dashboard:"
)
st_number_input = st.Page(
    "chapters/api-reference/input-widgets/number-input.py", title="st.number_input",
    icon=":material/dashboard:"
)
st_text_input = st.Page(
    "chapters/api-reference/input-widgets/text-input.py", title="st.text_input",
    icon=":material/dashboard:"
)
st_link_button = st.Page(
    "chapters/api-reference/input-widgets/link-button.py", title="st.link_button",
    icon=":material/dashboard:"
)
st_file_uploader = st.Page(
    "chapters/api-reference/input-widgets/file-uploader.py", title="st.file_uploader",
    icon=":material/dashboard:"
)

st_image = st.Page(
    "chapters/api-reference/media/image.py", title="st.image",
    icon=":material/dashboard:"
)
st_logo = st.Page(
    "chapters/api-reference/media/logo.py", title="st.logo",
    icon=":material/dashboard:"
)
st_audio = st.Page(
    "chapters/api-reference/media/audio.py", title="st.audio",
    icon=":material/dashboard:"
)
st_video = st.Page(
    "chapters/api-reference/media/video.py", title="st.video",
    icon=":material/dashboard:"
)

st_area_chart = st.Page(
    "chapters/api-reference/charts/area-chart.py", title="st.area_chart",
    icon=":material/dashboard:"
)
st_bar_chart = st.Page(
    "chapters/api-reference/charts/bar-chart.py", title="st.bar_chart",
    icon=":material/dashboard:"
)
st_line_chart = st.Page(
    "chapters/api-reference/charts/line-chart.py", title="st.line_chart",
    icon=":material/dashboard:"
)
st_scatter_chart = st.Page(
    "chapters/api-reference/charts/scatter-chart.py", title="st.scatter_chart",
    icon=":material/dashboard:"
)
st_map = st.Page(
    "chapters/api-reference/charts/map.py", title="st.map",
    icon=":material/dashboard:"
)

st_columns = st.Page(
    "chapters/api-reference/layouts/columns.py", title="st.columns",
    icon=":material/dashboard:"
)
st_empty = st.Page(
    "chapters/api-reference/layouts/empty.py", title="st.empty",
    icon=":material/dashboard:"
)

st_dataframe = st.Page(
    "chapters/api-reference/data/dataframe.py", title="st.dataframe",
    icon=":material/dashboard:"
)
st_data_editor = st.Page(
    "chapters/api-reference/data/data_editor.py", title="st.data_editor",
    icon=":material/dashboard:"
)
st_table = st.Page(
    "chapters/api-reference/data/table.py", title="st.table",
    icon=":material/dashboard:"
)
st_metric = st.Page(
    "chapters/api-reference/data/metric.py", title="st.metric",
    icon=":material/dashboard:"
)
st_json = st.Page(
    "chapters/api-reference/data/json.py", title="st.json",
    icon=":material/dashboard:"
)

pg = st.navigation(
    {
        "": [introduction],
        
        "🔶 Start": [install, create, run],

        "🔶 Text": [st_markdown, st_title, st_header, st_subheader, st_caption, st_code, st_latex, st_divider],

        "🔶 Write & magic": [st_write, st_write_stream, st_magic],

        "🔶 Input widgets": [
            st_button, st_checkbox, st_radio, st_rbc, st_selectbox, st_number_input, st_text_input,
            st_link_button, st_file_uploader],

        "🔶 Media elements": [st_image, st_logo, st_audio, st_video],

        "🔶 Chart elements": [st_area_chart, st_bar_chart, st_line_chart, st_scatter_chart, st_map],

        "🔶 Layouts": [st_columns, st_empty],

        "🔶 Data elements": [st_dataframe, st_data_editor, st_table, st_metric, st_json],
    },
)

pg.run()
