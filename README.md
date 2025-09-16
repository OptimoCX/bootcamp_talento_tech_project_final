Legalización Automática de Facturas y Comprobantes de Adjudicación
📌 Contexto
El proceso actual de legalización de anticipos y comprobantes en el sector de motos de segunda es manual: los asesores envían imágenes o PDFs, y el área contable debe clasificarlos y registrar la información.
Esto genera:
⏳ Alto consumo de tiempo (≈ 3 horas/día por persona).
❌ Mayor propensión a errores humanos.
📉 Baja escalabilidad frente al aumento de transacciones.
💸 Impacto negativo en inventario y flujo de caja.
🚀 Solución Propuesta: Clara
Un modelo híbrido que combina visión por computador y procesamiento de lenguaje natural para automatizar la clasificación y legalización de documentos.
Componentes del modelo:
OCR + Embeddings: extracción de texto (Tesseract) y conversión a embeddings (SentenceTransformer) para clasificación con Logistic Regression.
Computer Vision: uso de ResNet50 con data augmentation para diferenciar documentos por patrones visuales.
Fusión de probabilidades: combinación de ambos clasificadores para obtener la clase final con mayor precisión.
📊 Resultados
Precisión: >80% en clasificación de documentos.
Reducción de tiempos: 60–80%.
Trazabilidad y cumplimiento regulatorio.
Mejora en eficiencia operativa con menor reproceso y errores.
🔑 Ventajas Competitivas
Diseñado con conocimiento directo del sector motos de segunda.
Escalable y adaptable a otros sectores.
Futuro: integración con el software contable Logro para trazabilidad total.
🛠️ Metodología
Entendimiento del negocio y datos.
Preparación y etiquetado de documentos (PDF/JPG → 6 categorías).
Iteraciones con modelos CV + NLP.
Selección de modelo híbrido.
Despliegue práctico en Streamlit.
Evaluación con métricas (accuracy, confusion matrix).
📂 Estructura del Proyecto
/data → Documentos procesados y crudos.
/notebooks → Exploración y pruebas de modelos.
/src → Código de extracción OCR, embeddings, ResNet50 y fusión.
/app → Implementación en Streamlit.
👥 Autores
Julián Marulanda
Mariana Durán
Luisa Cano
Marcela Díaz
Walter Hernández
