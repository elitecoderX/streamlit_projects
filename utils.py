import streamlit as st
import os


@st.dialog("Comming soon...")
def comming_soon():
    st.write("The code is coming soon! Stay tuned.")
    if st.button("Ok"):
        st.rerun()

def add_project(title, description, button1_page, button2_url=None, button1_label="Try now 🚀", button2_label="Code 🧑‍💻"):
    with st.container(border=True):
        st.write(f':red[{title}]')
        st.write(description)
        col1, col2 = st.columns(2)
        with col1:
            if st.button(button1_label, type='primary', use_container_width=True):
                st.switch_page(os.path.join('pages', button1_page))
        with col2:
            if st.button(button2_label, use_container_width=True):
                if button2_url:
                    st.markdown(f'<meta http-equiv="refresh" content="0; url={button2_url}">', unsafe_allow_html=True)
                else:
                    comming_soon()