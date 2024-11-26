from scapy.all import sniff
import numpy as np
import sys
import os
from src.utils import load_trained_model  # Importa la función desde utils.py

# Agregar el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Llama a la función para cargar el modelo
model = load_trained_model("models/model.h5")

if model is not None:
    def process_packet(packet):
        if packet.haslayer("IP"):
            packet_data = {"bytes": len(packet)}
            normalized_data = np.array([[packet_data["bytes"] / 1500]])
            prediction = model.predict(normalized_data)
            decision_label = np.argmax(prediction, axis=1)[0]
            print(f"Paquete procesado - Decisión: {decision_label}")

    print("Capturando tráfico en tiempo real... (Ctrl+C para detener)")
    sniff(prn=process_packet, store=False)
else:
    print("No se pudo cargar el modelo. Asegúrate de tener el archivo 'model.h5' en la carpeta 'models'.")

