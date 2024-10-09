import streamlit as st


def home():
    st.title("Video Player App")

    # Add a video from an online source (e.g., YouTube or other video hosting services)
    video_url = "https://cdn.pixabay.com/video/2016/12/31/6962-197634410_large.mp4"

    # Display the video in the Streamlit app
    st.video(video_url)