import streamlit as st

st.title("My First web App")
name = st.text_input("Enter your name")

if st.button("Say Hello"):
    if name:
        st.success(f"Hello {name}, welcome to my page")
    else:
        st.warning("Please enter your Name")