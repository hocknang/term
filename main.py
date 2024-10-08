import streamlit as st
from streamlit_option_menu import option_menu

# Sidebar option menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",  # Required
        options=["Home", "About", "Contact"],  # Required
        icons=["house", "info", "envelope"],  # Optional, icons from FontAwesome
        menu_icon="cast",  # Optional
        default_index=0,  # Optional, sets the Home option as the default
    )

# Display selected page content
if selected == "Home":
    st.title("Welcome to the Home Page")
    st.write("This is the Home page of the app.")
elif selected == "About":
    st.title("About Us")
    st.write("Here is information about us.")
elif selected == "Contact":
    st.title("Contact Us")
    st.write("You can reach us via this page.")