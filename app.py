import os
import time
import subprocess

DEVICE_NAME = "BSD-BT"  # Ersetzen Sie dies durch den Namen Ihres Bluetooth-Geräts
DEVICE_MAC = "E1:0C:BF:28:84:33"  # Ersetzen Sie dies durch die MAC-Adresse Ihres Geräts

def is_device_connected(device_name, device_mac):
    result = subprocess.run(["system_profiler", "SPBluetoothDataType"], capture_output=True, text=True)
    # Sucht nach dem Gerätenamen und überprüft dann, ob "Connected: Yes" in den folgenden Zeilen steht
    if device_name in result.stdout:
        start = result.stdout.index(device_name)
        end = result.stdout.index("\n", start)
        return f"Connected: Yes" in result.stdout[start:end]
    return False

while True:
    if is_device_connected(DEVICE_NAME, DEVICE_MAC):
        print("\033[92mGerät ist verbunden.\033[0m")  # Grün
    else:
        print("\033[91mGerät ist nicht verbunden. Versuche zu verbinden...\033[0m")  # Rot
        # Ersetzen Sie diesen Befehl durch den Befehl, der auf Ihrem System eine Verbindung herstellt
        os.system(f"blueutil --connect {DEVICE_MAC}")
        print("\033[93mVerbindungsbefehl wurde ausgeführt.\033[0m")  # Gelb
    
    time.sleep(5)
