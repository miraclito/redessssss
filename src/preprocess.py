import pandas as pd

def preprocess_data(input_file="data/captured_packets.csv"):
    df = pd.read_csv(input_file)
    df["bytes_normalized"] = df["bytes"] / 1500  # Normalización (MTU máximo)
    return df[["bytes_normalized"]].values

if __name__ == "__main__":
    data = preprocess_data()
    print("Datos preprocesados:", data)
