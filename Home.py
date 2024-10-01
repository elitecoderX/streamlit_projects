import streamlit as st
from utils import add_project


st.set_page_config(
     page_title="elitecoderX - Home",
     initial_sidebar_state="collapsed",
     layout="centered",
 )

st.title(":red[Sachin]")

st.write("""
**Email:** [sachinprajapati09890@gmail.com](mailto:sachinprajapati09890@gmail.com)  
**LinkedIn:** [linkedin.com/in/sachin-elitecoderx](https://linkedin.com/in/sachin-elitecoderx)  
**GitHub:** [github.com/elitecoderX](https://github.com/elitecoderX)
""")

st.write("I hold a Bachelor of Science degree in Computer Science from Dayalbagh Educational Institute and am currently pursuing a Master’s degree in Computer Science.")
st.write("This repository showcases a collection of my projects, all deployed on Streamlit.")

st.divider()
st.header(':red[Projects]')

add_project(
    title="Image Compressor",
    description="This project implements image compression using DCT and DFT, transforming image patches to the frequency domain, applying quantization, and retaining key coefficients to balance between image quality and file size.",
    button1_page="1_Image_Compressor.py",
    button2_url=None
)
