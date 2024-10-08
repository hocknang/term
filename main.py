import streamlit as st
import empower as empower
import awards as awards
import asktadm as asktadm
import photo as photo


# Define the pages
def page_home():
    empower.home()


def page_chatbot():
   asktadm.home()

def page_awards():
    awards.home()


def page_photo_gallery():
    photo.home()


# Create a dictionary of pages
pages = {
    "EmPOWER": page_home,
    "ASK TADM": page_chatbot,
    "Awards And Events": page_awards,
    "Photo Gallery": page_photo_gallery
}

# Add a sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
page = pages[selection]
page()
