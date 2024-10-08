import streamlit as st

def home():
    st.write("a logo and text next to eachother")
    col1, mid, col2 = st.beta_columns([1, 1, 20])
    with col1:
        st.image('https://github.com/hocknang/term/blob/main/picture/tadm%20icon.png', width=60)
    with col2:
        st.write('A Name')
