import streamlit as st
from src.predict import predict_image
import os
import datetime


def display_prediction_section():
    """
    Display the prediction section with class and probability results.
    """

    st.header("Predicción del Documento")

    st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #4CAF50; /* Verde */
        color: white;
    }
    div.stButton > button:first-child:hover {
        background-color: #45a049;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Prediction button
    if st.button("🔍 Realizar Predicción", type="primary"):
        try:
            with st.spinner("Cargando modelos y realizando predicción..."):
                # Get the uploaded file path
                image_path = st.session_state["uploaded_file_path"]
                
                # Make prediction using the existing function
                clase_pred, max_proba = predict_image(
                    image_path=image_path,
                )
                max_proba = float(max_proba)  # Ensure max_proba is a float
                # Create prediction result dictionary
                prediction_result = {
                    "predicted_class": clase_pred,
                    "confidence": max_proba,
                    "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "filename": st.session_state.get("uploaded_file_name", "N/A")
                }
                
                # Store prediction in session state
                st.session_state["prediction_result"] = prediction_result
                
                # Add to prediction history
                if "prediction_history" not in st.session_state:
                    st.session_state["prediction_history"] = []
                st.session_state["prediction_history"].append(prediction_result)
                
        except Exception as e:
            st.error(f"❌ Error durante la predicción: {str(e)}")
            return
    
    # Display prediction results if available
    if "prediction_result" in st.session_state:
        display_prediction_results(st.session_state["prediction_result"])


def display_prediction_results(prediction_result):
    """
    Display the prediction results in a nice format.
    
    Args:
        prediction_result: Dictionary containing prediction results
    """
    st.success("✅ Predicción realizada exitosamente")
    
    # Create columns for better layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Resultado de la Clasificación")
        
        # Main prediction
        predicted_class = prediction_result.get("predicted_class", "N/A")
        confidence = prediction_result.get("confidence", 0.0)
        
        # Display main result with styling
        st.markdown(
            f"""
            <div style='padding: 20px; border-radius: 10px; background-color: #f0f8ff; border-left: 5px solid #1f77b4;'>
                <h3 style='color: #1f77b4; margin: 0;'>Clase Predicha</h3>
                <h2 style='color: #333; margin: 10px 0;'>{predicted_class}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Confidence level indicator
        st.subheader("Nivel de Confianza")
        progress_bar = st.progress(confidence)
        
        # Color-coded confidence level
        if confidence >= 0.75:
            confidence_level = "🟢 Alta"
            confidence_color = "green"
        elif confidence >= 0.60:
            confidence_level = "🟡 Media"
            confidence_color = "orange"
        else:
            confidence_level = "🔴 Baja"
            confidence_color = "red"
        
        st.markdown(
            f"<p style='color: {confidence_color}; font-weight: bold;'>{confidence_level} ({confidence:.1%})</p>",
            unsafe_allow_html=True
        )
    
    with col2:
        st.subheader("Información Adicional")
        
        # File info
        filename = prediction_result.get("filename", "N/A")
        st.info(f"📄 Archivo: {filename}")
        
        # Prediction timestamp
        timestamp = prediction_result.get("timestamp", "N/A")
        st.info(f"🕐 Predicción realizada: {timestamp}")
        
        # # Confidence score details
        # st.metric(
        #     label="Puntuación de Confianza",
        #     value=f"{confidence:.3f}",
        #     delta=f"{confidence:.1%}"
        # )
    
    # Additional model information
    with st.expander("ℹ️ Información del Modelo"):
        st.write("**Tipo de Modelo:** Clasificador Híbrido")
        st.write("**Componentes:**")
        st.write("• Modelo OCR para extracción de texto")
        st.write("• Modelo de embeddings para análisis semántico")
        st.write("• ResNet para análisis de imágenes")
        st.write("**Método:** Predicción basada en probabilidad máxima")
        
        # Show possible classes
        st.write("**Clases disponibles:**")
        possible_classes = ["Arreglos", "Impuesto_Vehicular", "Tecnomecanica", "Cuentas_Cobro", "SOAT", "Traspasos"]
        for cls in possible_classes:
            if cls == predicted_class:
                st.write(f"• **{cls}** ← Predicción actual")
            else:
                st.write(f"• {cls}")