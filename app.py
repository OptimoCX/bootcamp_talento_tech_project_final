import streamlit as st
from PIL import Image
import os
from display.login import verify_login
from display.configuration import configure_page
from display.upload import display_upload_section
from display.predict import display_prediction_section
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Application started.")
    configure_page()
    # Load business logo
    logo_left_path = "img/celerix_sas_logo.png"
    logo_right_path = "img/clara.png"

    col1, col2, col3 = st.columns([1, 6, 1])  # ajusta proporciones a gusto

    # Logo a la izquierda
    if os.path.exists(logo_left_path):
        with col3:
            logo_left = Image.open(logo_left_path)
            st.image(logo_left, width=300)

    # espacio vacío en el centro (col2)

    # Logo a la derecha
    if os.path.exists(logo_right_path):
        with col1:
            logo_right = Image.open(logo_right_path)
            st.image(logo_right, width=300)
    # st.markdown("<h1 style='text-align: center; color: #6A95FA; font-size: 2.5em; font-weight: bold;'>CLARA</h1>", unsafe_allow_html=True)
    # # Authentication
    # st.header("Autenticación")
    verify_login()
    st.success(f"Bienvenido, {st.session_state['usuario']}!")
    # if document_number:
    if st.session_state["logueado"]:

            #Subida documento
            display_upload_section()

            if st.session_state["uploaded_file"]:
                st.header("Segmentación")
                st.text("Esta sección te permite realizar la inferencia del documento subido")
                display_prediction_section()
    else:
        logging.warning("Unauthorized access attempt.")
        st.error("Número de documento no permitido. No puede acceder.")
        st.stop()

if __name__ == "__main__":
    main()
