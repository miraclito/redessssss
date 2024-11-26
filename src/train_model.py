from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

def load_data(input_file="data/captured_packets.csv"):
    # Leer el archivo CSV
    df = pd.read_csv(input_file)
    # Normalizar los tamaños de los paquetes
    X = df["bytes"].values.reshape(-1, 1) / 1500  # Normalización de bytes
    # Convertir etiquetas a formato one-hot encoding (asegúrate de que la columna 'labels' exista)
    y = df["labels"].values  # Etiquetas: 0 (Normal), 1 (Sospechoso), 2 (Malicioso)
    y = np.eye(3)[y]  # Codificar etiquetas como one-hot
    return X, y

def train_model():
    # Cargar los datos
    X, y = load_data()

    # Dividir los datos en entrenamiento y prueba (80% entrenamiento, 20% prueba)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crear un modelo básico
    model = Sequential([
        Dense(32, activation='relu', input_shape=(1,)),  # Capa oculta con 32 nodos
        Dense(16, activation='relu'),                   # Segunda capa oculta
        Dense(3, activation='softmax')                  # Capa de salida (3 clases)
    ])

    # Compilar el modelo
    model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

    # Entrenar el modelo
    print("Iniciando el entrenamiento...")
    model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=1)

    # Evaluar el modelo con los datos de prueba
    print("Evaluando el modelo con los datos de prueba...")
    test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=1)
    print(f"Precisión en el conjunto de prueba: {test_accuracy * 100:.2f}%")

    # Guardar el modelo en models/model.h5
    model.save("models/model.h5")
    print("Entrenamiento completado. Modelo guardado en models/model.h5")

if __name__ == "__main__":
    train_model()
