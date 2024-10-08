import streamlit as st

# Define the pages
def page_home():
    st.title("Home")
    st.write("Welcome to the Home Page.")
    st.write("Welcome to the Home Page.")
    st.write("Welcome to the Home Page.")


def page_about():
    st.title("About")
    st.write("This is the About Page.")

def page_contact():
    st.title("Contact")
    st.write("Here is the Contact Page.")

# Create a dictionary of pages
pages = {
    "Home": page_home,
    "About": page_about,
    "Contact": page_contact
}

# Add a sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
page = pages[selection]
page()