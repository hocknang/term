import streamlit as st
import empower as empower


# Define the pages
def page_home():
    empower.home()

def page_about():
    st.title("About")
    st.write("This is the About Page.")


def page_awards():
    st.title("Awards")
    st.write("Here is the Contact Page.")


# Create a dictionary of pages
pages = {
    "EmPOWER": page_home,
    "ASK TADM": page_about,
    "Awards": page_awards
}

# Add a sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
page = pages[selection]
page()
