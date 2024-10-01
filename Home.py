import streamlit as st
import os


st.set_page_config(
     page_title="elitecoderX - Home",
     layout="centered",
     initial_sidebar_state="auto"
 )

st.title(":red[Sachin Prajapati]")

st.write("""
**Email:** [sachinprajapati09890@gmail.com](mailto:sachinprajapati09890@gmail.com)  
**LinkedIn:** [linkedin.com/in/sachin-elitecoderx](https://linkedin.com/in/sachin-elitecoderx)  
**GitHub:** [github.com/elitecoderX](https://github.com/elitecoderX)
""")

st.write("""
I am a Master’s student in Computer Science at Dayalbagh Educational Institute, specializing in machine learning and web development.
With expertise in Python, TensorFlow, OpenCV, and Streamlit, I am passionate about AI-driven solutions and aim to contribute impactful research to the field of artificial intelligence.
""")

st.divider()
st.header(':red[Projects]')

with st.container(border=True):
    st.write(':red[Image Compressor]')
    st.write('This project implements image compression using DCT and DFT, transforming image patches to the frequency domain, applying quantization, and retaining key coefficients to balance between image quality and file size.')
    if st.button('Try now 🚀', type='secondary'):
        st.switch_page(os.path.join('pages','1_Image_Compressor.py'))