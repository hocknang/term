import streamlit as st


def home():
    st.title("Video Player App")

    # Add a video from an online source (e.g., YouTube or other video hosting services)
    video_url = "https://pixabay.com/en/videos/star-long-exposure-starry-sky-sky-6962/"

    # Display the video in the Streamlit app
    st.video(video_url)