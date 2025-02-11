import streamlit as st

st.title("🔷 st.video()")

st.divider()

st.write('''
- Display a video player
''')

st.divider()

code = '''
video_file = open("chapters/api-reference/media/myvideo.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes, subtitles={
    "English vtt": "chapters/api-reference/media/myvideo.vtt",
    "English srt": "chapters/api-reference/media/myvideo.srt"})
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

video_file = open("chapters/api-reference/media/myvideo.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes, subtitles={
    "English vtt": "chapters/api-reference/media/myvideo.vtt",
    "English srt": "chapters/api-reference/media/myvideo.srt"})

st.divider()

code = '''
subtitles = st.file_uploader("Upload subtitles", accept_multiple_files=True)
if subtitles:
    st.video("chapters/api-reference/media/myvideo.mp4", subtitles={file.name: file for file in subtitles})
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

subtitles = st.file_uploader("Upload subtitles", accept_multiple_files=True)
if subtitles:
    st.video("chapters/api-reference/media/myvideo.mp4", subtitles={file.name: file for file in subtitles})
