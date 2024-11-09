import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
import os

# Load environment variables
load_dotenv()

# Configure the Generative AI model API
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

# Function to generate a response from text and/or image input
def generate_response(text_input, image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    if text_input and image:
        response = model.generate_content([text_input, image])
    elif text_input:
        response = model.generate_content(text_input)
    elif image:
        response = model.generate_content(image)
    else:
        return "Please provide an image and/or text."
    
    return response.text if response else "No response generated."

# Streamlit UI
st.set_page_config(page_title="AI Image-to-Text", page_icon="✨")

# Title and Banner
st.markdown(
    """
    <style>
    .main-title { 
        text-align: center; 
        font-size: 32px; 
        color: #4CAF50; 
        margin-top: 20px;
    }
    .footer { 
        text-align: center; 
        color: #888; 
        font-size: 12px; 
        margin-top: 20px; 
    }
    </style>
    <h1 class="main-title">✨ AI Image-to-Text Assistant ✨</h1>
    <p style="text-align: center;">Upload an image or enter a prompt to get AI-powered insights!</p>
    """, 
    unsafe_allow_html=True
)

# Image Upload Section
st.markdown("### 📷 Upload an Image")
uploaded_file = st.file_uploader("Upload an Image (jpg, jpeg, png):", type=['jpg', 'jpeg', 'png'])
image = None

# Image Processing
if uploaded_file:
    # Load the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

# Text Input Section
text_input = st.text_input("📝 Enter a prompt (optional):")

# Generate Response Button
if st.button("✨ Generate Response"):
    if not uploaded_file and not text_input:
        st.warning("Please upload an image or enter a prompt.")
    else:
        with st.spinner("Processing... Please wait..."):
            result = generate_response(text_input, image)
        st.write("### 🎉 Your AI-Generated Response:")
        st.write(result)  # This will print the response in a normal way without a box

# Footer
st.markdown(
    """
    <div class="footer">
        <p>Powered by <strong>Google’s Gemini AI</strong>. This app is for informational use only.</p>
    </div>
    """,
    unsafe_allow_html=True
)
