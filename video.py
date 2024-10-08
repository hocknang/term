import streamlit as st


def home():
    video_file = open("https://www.youtube.com/watch?v=u_C-UpCaRFM", "rb")
    video_bytes = video_file.read()

    st.video(video_bytes)