from scapy.all import sniff
import pandas as pd

def classify_packet(packet_size):
    """
    Función para clasificar los paquetes según su tamaño.
    - 0: Normal (Paquetes pequeños)
    - 1: Sospechoso (Paquetes medianos)
    - 2: Malicioso (Paquetes grandes)
    """
    if packet_size <= 500:
        return 0  # Normal
    elif 500 < packet_size <= 1500:
        return 1  # Sospechoso
    else:
        return 2  # Malicioso

def capture_packets(output_file="data/captured_packets.csv", count=100):
    def process_packet(packet):
        if packet.haslayer("IP"):
            packet_size = len(packet)
            packet_data = {
                "src": packet["IP"].src,
                "dst": packet["IP"].dst,
                "bytes": packet_size,
                "labels": classify_packet(packet_size)  # Asignar etiqueta en función del tamaño del paquete
            }
            captured_packets.append(packet_data)
    
    captured_packets = []
    sniff(prn=process_packet, count=count, store=False)
    
    # Guardar en un archivo CSV
    df = pd.DataFrame(captured_packets)
    df.to_csv(output_file, index=False)
    print(f"Paquetes capturados y guardados en {output_file}")

if __name__ == "__main__":
    capture_packets()
