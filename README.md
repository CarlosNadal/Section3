███████╗███████╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗██████╗ 

██╔════╝██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║╚════██╗

███████╗█████╗  ██║        ██║   ██║██║   ██║██╔██╗ ██║ █████╔╝

╚════██║██╔══╝  ██║        ██║   ██║██║   ██║██║╚██╗██║ ╚═══██╗

███████╗███████╗╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║██████╔╝
╚══════╝╚══════╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ 
             SECTION3 — Wireless Arsenal · by Karli
             
## 🔥 ¿Qué es Section 3?

**Section 3** es una suite de herramientas y notas diseñadas para pentesting WiFi, enfocada en la exploración, explotación y protección de redes inalámbricas.  
Creado con enfoque realista, portátil y automatizable, pensado tanto para red teamers como para defensores que quieran entender las reglas del juego.

---

## 📂 Contenido del repositorio

- 🎯 Scripts de escaneo, recolección y ataque
- 🧠 Notas técnicas sobre 802.11, canales, encriptación, tramas, contramedidas, etc.
- 🛡️ Hardening automatizado de APs y estaciones
- 🧪 Experimentos y pruebas reales con AWUS1900
- 🧱 Código modular para integrar en dashboards o interfaces web (FastAPI, React, Docker)
- 📁 Capturas `.cap` de handshakes y análisis (solo con fines educativos)

---

## 🛠️ Tecnologías usadas

- **Linux (Kali, Debian-based)**
- **Aircrack-ng**, **airodump-ng**, **aireplay-ng**
- **TShark**, **tcpdump**, **Bettercap**
- **Python**, **Bash**
- **Docker** (para contenedores reproducibles)

---

## ⚙️ Requisitos

- Antena compatible con modo monitor (recomendado: **Alfa AWUS1900**)
- Permisos de root
- Paquetes esenciales:
  
```bash
sudo apt install aircrack-ng tshark net-tools
