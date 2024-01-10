import streamlit as st
import pandas as pd

col1, col2 = st.columns(2)

with col1:
    st.header("Hi, I am Chelsey")
    st.subheader("Education")
    st.write("University of Washington - Technology Innovation")
    st.subheader("Work Experience")
    st.write("Techinical Support Assistant @ GIX")
    st.subheader("Hobbies")
    st.write("Sleep")
    st.subheader("Interesting project")
    st.write("none")

with col2:
   st.image('chelsey.JPG', caption='Me')