import streamlit as st
import os
from PIL import Image
import google.generativeai as genai


#genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

genai.configure(api_key="AIzaSyAu9czvI-w-CJ-OAlXrfaO-LYOxGT08kN0")
model=genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return(response.text)

st.set_page_config(page_title="Tell me About Image Demo")
st.header("My First Gemini Image LLM Application")
input=st.text_input("Input: ",key="input")

uploaded_file=st.file_uploader("Choose an image...",type=["jpg","jpeg","png"])
image=""

if uploaded_file:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded image",use_column_width=True)

submit=st.button("Tell me about image..")
if submit:
    response=get_gemini_response(input,image)
    st.write(response)
