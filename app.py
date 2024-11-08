import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
from PIL import Image

import os
import textwrap


# Setup the API

genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

def generate_response(input,image):
    model=genai.GenerativeModel("gemini-1.5-flash")
    if input != "":
        if image is not None:
            response = model.generate_content([input,image])
            return response.text
        else:
            response = model.generate_content(input)
            return response.text

    elif image !="":
        
        response = model.generate_content(image)
        return response.text

    else:
        return "Please Enter the Image and Text"

st.header("Image to :blue[Text]")
upload_file=st.file_uploader("Upload an Image ",type=['jpg','jpeg','png'])
image=''
if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image,caption='Uploaded Image',use_container_width=True)
input = st.text_input("Enter the Prompt")

submit=st.button("Do the Magic")


if submit:
    res=generate_response(input,image)
    st.write("The Response is")
    st.markdown(res)