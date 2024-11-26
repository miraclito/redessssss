import os
from tensorflow.keras.models import load_model

def load_trained_model(model_path="models/model.h5"):
    """
    Carga el modelo entrenado desde el archivo proporcionado.

    Args:
    - model_path: Ruta al archivo .h5 del modelo entrenado.

    Returns:
    - El modelo cargado si el archivo existe, de lo contrario, None.
    """
    if os.path.exists(model_path):
        model = load_model(model_path)
        print(f"Modelo cargado desde {model_path}")
        return model
    else:
        print(f"Error: El archivo {model_path} no se encuentra en la ubicación especificada.")
        return None
