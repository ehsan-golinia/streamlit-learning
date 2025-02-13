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
st_select_slider = st.Page(
    "chapters/api-reference/input-widgets/select-slider.py", title="st.select_slider",
    icon=":material/dashboard:"
)
st_slider = st.Page(
    "chapters/api-reference/input-widgets/slider.py", title="st.slider",
    icon=":material/dashboard:"
)
st_date_input = st.Page(
    "chapters/api-reference/input-widgets/date-input.py", title="st.date_input",
    icon=":material/dashboard:"
)
st_time_input = st.Page(
    "chapters/api-reference/input-widgets/time-input.py", title="st.time_input",
    icon=":material/dashboard:"
)
st_text_input = st.Page(
    "chapters/api-reference/input-widgets/text-input.py", title="st.text_input",
    icon=":material/dashboard:"
)
st_text_area = st.Page(
    "chapters/api-reference/input-widgets/text-area.py", title="st.text_area",
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
st_pyplot = st.Page(
    "chapters/api-reference/charts/pyplot.py", title="st.pyplot",
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

st_progress = st.Page(
    "chapters/api-reference/status/progress.py", title="st.progress",
    icon=":material/dashboard:"
)
st_spinner = st.Page(
    "chapters/api-reference/status/spinner.py", title="st.spinner",
    icon=":material/dashboard:"
)
st_status = st.Page(
    "chapters/api-reference/status/status.py", title="st.status",
    icon=":material/dashboard:"
)
st_toast = st.Page(
    "chapters/api-reference/status/toast.py", title="st.toast",
    icon=":material/dashboard:"
)
st_balloons = st.Page(
    "chapters/api-reference/status/balloons.py", title="st.balloons",
    icon=":material/dashboard:"
)
st_snow = st.Page(
    "chapters/api-reference/status/snow.py", title="st.snow",
    icon=":material/dashboard:"
)
st_success = st.Page(
    "chapters/api-reference/status/success.py", title="st.success",
    icon=":material/dashboard:"
)
st_info = st.Page(
    "chapters/api-reference/status/info.py", title="st.info",
    icon=":material/dashboard:"
)
st_warning = st.Page(
    "chapters/api-reference/status/warning.py", title="st.warning",
    icon=":material/dashboard:"
)
st_error = st.Page(
    "chapters/api-reference/status/error.py", title="st.error",
    icon=":material/dashboard:"
)
st_exception = st.Page(
    "chapters/api-reference/status/exception.py", title="st.exception",
    icon=":material/dashboard:"
)

st_form = st.Page(
    "chapters/api-reference/execution-flow/form.py", title="st.form",
    icon=":material/dashboard:"
)
st_form_submit_button = st.Page(
    "chapters/api-reference/execution-flow/form-submit-button.py", title="st.form_submit_button",
    icon=":material/dashboard:"
)
user_form = st.Page(
    "chapters/api-reference/execution-flow/user-form.py", title="User Form",
    icon=":material/dashboard:"
)

pg = st.navigation(
    {
        "": [introduction],
        
        "🔶 Start": [install, create, run],

        "🔶 Text": [st_markdown, st_title, st_header, st_subheader, st_caption, st_code, st_latex, st_divider],

        "🔶 Write & magic": [st_write, st_write_stream, st_magic],

        "🔶 Input widgets": [
            st_button, st_checkbox, st_radio, st_rbc, st_selectbox, st_number_input, st_select_slider,
            st_slider, st_date_input, st_time_input, st_text_input, st_text_area, st_link_button, st_file_uploader],

        "🔶 Media elements": [st_image, st_logo, st_audio, st_video],

        "🔶 Chart elements": [st_area_chart, st_bar_chart, st_line_chart, st_scatter_chart, st_map, st_pyplot],

        "🔶 Layouts": [st_columns, st_empty],

        "🔶 Data elements": [st_dataframe, st_data_editor, st_table, st_metric, st_json],

        "🔶 Progress and status": [
            st_progress, st_spinner, st_status, st_toast, st_balloons, st_snow,
            st_success, st_info, st_warning, st_error, st_exception],

        "🔶 Execution flow": [st_form, st_form_submit_button, user_form],
    },
)

pg.run()
