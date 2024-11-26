import pandas as pd  # Asegúrate de importar pandas

from src.capture import capture_packets
from src.preprocess import preprocess_data
from src.train_model import train_model
from src.visualize import visualize_data
from src.capture_and_decision import process_packet
import subprocess

def export_to_excel(input_file="data/captured_packets.csv", output_file="data/captured_packets.xlsx"):
    # Leer el archivo CSV
    df = pd.read_csv(input_file)
    
    # Exportar los datos a un archivo Excel
    df.to_excel(output_file, index=False)
    print(f"Datos exportados a {output_file}")

def main():
    while True:
        print("Opciones:")
        print("1. Capturar tráfico")
        print("2. Preprocesar datos")
        print("3. Entrenar modelo")
        print("4. Visualizar datos")
        print("5. Captura y decisión en tiempo real")
        print("6. exportar en excel")
        print("7. Salir")
        
        choice = input("Selecciona una opción: ")
        
        if choice == "1":
            capture_packets()
        elif choice == "2":
            preprocess_data()
        elif choice == "3":
            train_model()
        elif choice == "4":
            visualize_data()
        elif choice == "5":
            try:
                print("Iniciando captura en tiempo real... Presiona Ctrl+C para detener.")
                subprocess.run(["python", "-m", "src.capture_and_decision"], check=True)
            except KeyboardInterrupt:
                print("\nCaptura en tiempo real detenida.")
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar src.capture_and_decision: {e}")
        elif choice == "6":
            export_to_excel()  # Llamada a la función para exportar los datos a Excel
        elif choice == "7":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Llamar al main para que se ejecute el programa
if __name__ == "__main__":
    main()
