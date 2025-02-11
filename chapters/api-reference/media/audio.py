import streamlit as st
import numpy as np

st.title("🔷 st.audio()")

st.divider()

st.write('''
- Display an audio player
''')

st.divider()

code = '''
st.audio("chapters/api-reference/media/meow.mp3", format="audio/mpeg", loop=True)
'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

st.audio("chapters/api-reference/media/meow.mp3", format="audio/mpeg", loop=True)

st.divider()

code = '''audio_file = open("chapters/api-reference/media/meow.mp3", "rb")
audio_bytes = audio_file.read()

st.audio(audio_bytes, format="audio/mpeg")

sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

st.audio(note_la, sample_rate=sample_rate)'''
st.code(code, language="python")

st.markdown(":orange[Output:]")

audio_file = open("chapters/api-reference/media/meow.mp3", "rb")
audio_bytes = audio_file.read()

st.audio(audio_bytes, format="audio/mpeg")

sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

st.audio(note_la, sample_rate=sample_rate)
