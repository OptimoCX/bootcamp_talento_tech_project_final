import streamlit as st
from parameters.allowed_ids import ALLOWED_IDS

def login():
    """
    Display the login screen and handle user authentication.
    """
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #E3F2FD; /* Light blue background */
            }

            .login-box {
                max-width: 400px;
                margin: auto;
                padding: 30px;
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }

            .stTextInput > div > div > input {
                background-color: #ffffff;
                color: #333;
                border-radius: 8px;
                padding: 10px;
            }

            .stButton > button {
                background-color: #4A148C; /* Blue button */
                color: white;
                border-radius: 8px;
                padding: 10px 20px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(
            """
            <h1 style='text-align: center; color: #4A148C; font-size: 1.5em; font-weight: 600;'>
                Bienvenido a CLARA
            </h1>
            <p style='text-align: center; color: #A9A9A9; font-size: 1.1em;'>
                Por favor, ingresa tus credenciales para continuar
            </p>
            """,
            unsafe_allow_html=True
        )

        email = st.text_input("Correo", placeholder="Ingrese su correo electrónico")
        password = st.text_input("Contraseña", type="password", placeholder="Ingrese su contraseña")
        login_boton = st.button("Ingresar")

    if login_boton:
        if email in ALLOWED_IDS and ALLOWED_IDS[email]["password"] == password:
            st.session_state["logueado"] = True
            st.session_state["usuario"] = ALLOWED_IDS[email]["name"]
            st.rerun()
        else:
            st.error("Correo o contraseña incorrectos")

def verify_login():
    """
    Verify if the user is logged in, otherwise display the login screen.
    """
    if "logueado" not in st.session_state:
        st.session_state["logueado"] = False
    if not st.session_state["logueado"]:
        login()
        st.stop()
