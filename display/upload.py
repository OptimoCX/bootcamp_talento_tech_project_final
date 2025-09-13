import streamlit as st
from src.file_processing import process_file

def display_upload_section():
    """
    Display the file upload section.
    """
    st.header("Subir documento")
    uploaded_file = st.file_uploader("Suba un archivo (PDF o Imagen)", type=["pdf", "png", "jpg", "jpeg"])

    if "uploaded_file" not in st.session_state:
        st.session_state["uploaded_file"] = False

    if uploaded_file:
        with st.spinner("Procesando archivo..."):
            jpg_path, uploaded_file_name = process_file(uploaded_file)
        st.session_state["uploaded_file_path"] = jpg_path
        st.session_state["uploaded_file_name"] = uploaded_file_name
        st.session_state["uploaded_file"] = True
        # st.rerun()

    if not st.session_state["uploaded_file"]:
        st.warning("Por favor, suba un archivo para continuar.")
    else:
        st.header("Documento subido exitosamente.")
        st.success(f"Archivo procesado exitosamente: {st.session_state['uploaded_file_name']}")

