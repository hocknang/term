import streamlit as st


def home():
    st.title("Video")

    # Add a video from an online source (e.g., YouTube or other video hosting services)
    video_url = "https://www.dropbox.com/scl/fi/b17vgeq6hmj92sy5xr8op/demoVideo.mp4?rlkey=551t3mndi0rxiowjw6ei3s2d6&st=n16gwygh&dl=0"

    # Display the video in the Streamlit app
    st.video(video_url)
