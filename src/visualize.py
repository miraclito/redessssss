import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(input_file="data/captured_packets.csv"):
    df = pd.read_csv(input_file)
    plt.figure(figsize=(10, 6))
    plt.hist(df["bytes"], bins=20, color="blue", alpha=0.7)
    plt.title("Distribución de tamaño de paquetes")
    plt.xlabel("Tamaño (bytes)")
    plt.ylabel("Frecuencia")
    plt.show()

if __name__ == "__main__":
    visualize_data()
