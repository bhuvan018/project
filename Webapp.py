import streamlit as st
from PIL import Image
import time as t


st.set_page_config(layout="wide")
    
st.title("Sketch to Image")
    
col1, col2 = st.columns([2, 3], gap="large")
    
with col1:
       
    uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
       
    text_prompt = st.text_area("Text Prompt")
        
        
    if st.button("Submit"):
        with st.spinner("Processing....."):
            t.sleep(5)
    
with col2:
        
    st.header("Output Image")
    st.image("https://via.placeholder.com/400x300?text=GAN+Output", use_column_width=True)
    
  
    if st.button("Download Image"):
        st.write("Download started")
