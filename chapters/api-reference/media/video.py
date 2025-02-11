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

st.video(video_bytes, subtitles="chapters/api-reference/media/myvideo.vtt")
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

video_file = open("chapters/api-reference/media/myvideo.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes, subtitles="chapters/api-reference/media/myvideo.vtt")
