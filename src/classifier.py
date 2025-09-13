import numpy as np
import joblib
import pytesseract
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
from sentence_transformers import SentenceTransformer

class HybridClassifierMaxProb:
    def __init__(self, ocr_model_path, embed_model_path, resnet_model_path):
        # cargar OCR + texto
        self.clf_text = joblib.load(ocr_model_path)
        self.modelo_embed = SentenceTransformer(embed_model_path)

        # cargar ResNet (keras)
        self.model_resnet = load_model(resnet_model_path, compile=False)

        # Clases
        self.clases_texto = ["Arreglos", "Impuesto_Vehicular", "Tecnomecanica"]
        self.clases_resnet = ["Cuentas_Cobro", "SOAT", "Traspasos"]

        # Preprocesamiento imágenes
        self.img_size = (224,224)
        self.normalization_layer = tf.keras.layers.Rescaling(1./255)

    def ocr_extract_text(self, image_path):
        try:
            img = Image.open(image_path)
            try:
                text = pytesseract.image_to_string(img, lang="spa")
            except:
                text = pytesseract.image_to_string(img, lang="eng")
            return text.strip()
        except Exception as e:
            print(f"Error con {image_path}: {e}")
            return ""

    def predict(self, image_path):
        # Probabilidades iniciales en 6 clases
        probas_total = {c: 0.0 for c in (self.clases_texto + self.clases_resnet)}

        # Paso 1: OCR + NLP
        texto = self.ocr_extract_text(image_path)
        if texto:
            embedding = self.modelo_embed.encode([texto])
            probas_text = self.clf_text.predict_proba(embedding)[0]
            for i, c in enumerate(self.clf_text.classes_):
                probas_total[c] = probas_text[i]

        # Paso 2: ResNet
        img = tf.keras.utils.load_img(image_path, target_size=self.img_size)
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)  # batch
        img_array = self.normalization_layer(img_array)

        probas_resnet = self.model_resnet.predict(img_array)[0]
        for i, c in enumerate(self.clases_resnet):
            probas_total[c] = probas_resnet[i]

        # Paso 3: escoger la clase con mayor probabilidad
        clase_pred = max(probas_total, key=probas_total.get)
        max_proba = probas_total[clase_pred]

        print(f"{clase_pred} (confianza {max_proba:.2f})")
        return clase_pred, max_proba
