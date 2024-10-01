import streamlit as st
from PIL import Image
from transform_coding import compress_img, MSE, get_image_size
import numpy as np
from io import BytesIO
import pandas as pd

st.title(':red[Image Compressor]')

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])
t_mode = st.selectbox("Select Transformation Mode", options=["DCT", "FFT"])

col1, col2 = st.columns(2)
with col1:
    patch_size = st.slider("Select Patch Size (nxn)", min_value=4, max_value=64, value=8, step=4)
with col2:
    q_level = st.slider("Select Retained Coefficient (%)", min_value=1, max_value=100, value=1)

compress = st.button("Compress", type='primary', use_container_width=True)

st.divider()

if "compressed_results" not in st.session_state:
    st.session_state.compressed_results = {}

if uploaded_file is not None:
    if compress or "img" in st.session_state.compressed_results:
        if compress:
            # Perform compression
            img, comp_img = compress_img(uploaded_file, patch_size, t_mode, q_level)
            mse_value = MSE(img, comp_img)
            img = Image.fromarray(img.astype(np.uint8))
            comp_img = Image.fromarray(comp_img.astype(np.uint8))
            original_size = get_image_size(img)
            compressed_size = get_image_size(comp_img)

            # Store the compression results in session state
            st.session_state.compressed_results = {
                "img": img,
                "comp_img": comp_img,
                "mse_value": mse_value,
                "original_size": original_size,
                "compressed_size": compressed_size,
            }
        else:
            # Retrieve the stored results from session state
            img = st.session_state.compressed_results["img"]
            comp_img = st.session_state.compressed_results["comp_img"]
            mse_value = st.session_state.compressed_results["mse_value"]
            original_size = st.session_state.compressed_results["original_size"]
            compressed_size = st.session_state.compressed_results["compressed_size"]

        data = {
            "Metric": ["Original Image Size (KB)", "Compressed Image Size (KB)", "Mean Square Error"],
            "Value": [f"{original_size:.2f}", f"{compressed_size:.2f}", f"{mse_value:.2f}"]
        }
    
        df = pd.DataFrame(data)
        st.write(":red[Compression Results:]")
        st.dataframe(df.style.hide(axis='index'), use_container_width=True)
    
        col1, col2 = st.columns(2)
    
        with col1:
            st.image(img, caption="Original Image", use_column_width=True)
            buf = BytesIO()
            img.save(buf, format="JPEG")
            byte_im = buf.getvalue()
            st.download_button(
                label="Download Original Image",
                data=byte_im,
                file_name="image.jpg",
                mime="image/jpeg",
                use_container_width=True
            )
            
        with col2:
            st.image(comp_img, caption="Compressed Image", use_column_width=True)
            buf = BytesIO()
            comp_img.save(buf, format="JPEG")
            byte_im = buf.getvalue()
            st.download_button(
                label="Download Compressed Image",
                data=byte_im,
                file_name="compressed_image.jpg",
                mime="image/jpeg",
                use_container_width=True
            )
