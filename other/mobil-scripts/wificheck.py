import time
from pywifi import PyWiFi, const, Profile

def scan_wifi():
    # WiFi interfész inicializálása
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]  # Az első hálózati interfész kiválasztása

    # Ha nincs interfész, jelezd
    if iface is None:
        print("Nincs elérhető Wi-Fi interfész.")
        return

    # Szkennelés indítása
    iface.scan()
    print("Hálózatok keresése...")

    time.sleep(3)  # Várj, amíg a szkennelés befejeződik
    results = iface.scan_results()

    # Talált hálózatok listázása
    print("\nElérhető Wi-Fi hálózatok:")
    for network in results:
        print(f"SSID: {network.ssid}, Jelerősség: {network.signal} dBm")

if __name__ == "__main__":
    scan_wifi()
