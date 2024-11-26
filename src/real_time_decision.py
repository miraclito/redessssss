from scapy.all import sniff
from tensorflow.keras.models import load_model
import numpy as np

# Mapeo de las clases a sus etiquetas
class_labels = {0: "Normal", 1: "Sospechoso", 2: "Malicioso"}

# Cargar el modelo
model = load_model("models/model.h5")

# Función para procesar cada paquete
def process_packet(packet):
    if packet.haslayer("IP"):  # Verificar si el paquete tiene capa IP
        packet_data = {"bytes": len(packet)}  # Extraer la longitud del paquete
        decision_label = real_time_decision(model, packet_data)  # Obtener la decisión
        print(f"Paquete procesado - Decisión: {decision_label}")

# Función para realizar la predicción en tiempo real
def real_time_decision(model, packet_data):
    normalized_data = np.array([[packet_data["bytes"] / 1500]])  # Normalizar los datos
    prediction = model.predict(normalized_data)  # Hacer la predicción
    decision_label = np.argmax(prediction, axis=1)[0]  # Obtener la clase con la mayor probabilidad
    return class_labels[decision_label]  # Devolver la etiqueta en lugar del número

# Iniciar la captura en tiempo real
print("Capturando tráfico en tiempo real... (Ctrl+C para detener)")
sniff(prn=process_packet, store=False)

