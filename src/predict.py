from src.classifier import HybridClassifierMaxProb


def predict_image(
    image_path,
    ocr_model_path="/Users/jmarulanda/clara/models/clasificador_texto.pkl",
    embed_model_path="/Users/jmarulanda/clara/models/modelo_embeddings",
    resnet_model_path="/Users/jmarulanda/clara/models/resnet_model.h5",
):
    classifier = HybridClassifierMaxProb(
        ocr_model_path, embed_model_path, resnet_model_path
    )
    clase_pred, max_proba = classifier.predict(image_path)
    return clase_pred, max_proba
