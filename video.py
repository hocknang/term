import streamlit as st


def home():
    video_file = open("https://pixabay.com/en/videos/star-long-exposure-starry-sky-sky-6962/", "rb")
    video_bytes = video_file.read()

    st.video(video_bytes)