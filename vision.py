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

st.header("Generative AI Application using Gemini Pro LLM Model.. ")
st.write('''Developed an application using the Gemini Pro model, a powerful Large Language Model (LLM), to demonstrate its capabilities. The app allows users to upload an image and performs three functions: identifying objects within the image, generating a summary of its content, and answering user questions related to the image. This showcases the integration of visual recognition and natural language processing in AI solutions.
''')


image=""
#cam_click=st.button("Click to Open Camera...")
#if cam_click:
uploaded_file=st.file_uploader("Choose an image...",type=["jpg","jpeg","png"])
if uploaded_file:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded image",use_column_width=True)

st.write("Or")
cam_input=st.camera_input("Upload the image using camera...",key="cam_input")
if cam_input:
    image=Image.open(cam_input)
    st.image(image,caption="Uploaded image",use_column_width=True)
   

input=st.text_input("Ask the Question related to Uploaded image (its Optional)",key="input")

submit=st.button("Provide insights about this image..")
if submit:
    response=get_gemini_response(input,image)
    st.write(response)
st.write("--------------------------------------------------------------------------------------------")
st.write("Developed by Sandeep Monga")