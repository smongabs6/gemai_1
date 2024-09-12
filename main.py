import streamlit as st

st.write("Welcome to Large Language Model(LLM) project using Gemini Pro Model..")
st.write("In this we have created two type of application")
st.write("1. You can ask any Question..")
st.write("2. You can upload the image and ask any Question for that image..")

st.link_button("Image based application","vision.py")
st.markdown('<a href="src/app" target="_self">Question and Answer</a>', unsafe_allow_html=True)
#st.page_link("pages/app.py",label="Question and Answer")
#st.page_link("pages/vision.py",label="Question on uploaded image")