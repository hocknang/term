import streamlit as st
import empower as empower
import awards as awards
import asktadm as asktadm
import photo as photo
import uPhoto as uPhoto
import video as video
import question as question
import locateUs as locateUs


# Define the pages
def page_home():
    empower.home()


def page_chatbot():
    asktadm.home()


def page_awards():
    awards.home()


def page_photo_gallery():
    photo.home()


def page_upload_photo():
    uPhoto.home()


def page_video():
    video.home()

def page_question():
    question.home()

def page_location():
    locateUs.home()


# Create a dictionary of pages
pages = {
    "EmPOWER": page_home,
    "ASK TADM": page_chatbot,
    "Awards And Events": page_awards,
    "Video": page_video,
    "MCQ Question": page_question,
    "Locate Us": page_location
}

# Add a sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
page = pages[selection]
page()
