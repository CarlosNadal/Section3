#!/bin/bash

# Script para activar modo monitor en wlan0 usando airmon-ng correctamente

if [ "$#" -ne 1 ]; then
	echo "❌ Uso incorrecto."
	echo "✅ Uso correcto: $0 <interfaz_monitor>"
	echo "Ejemplo: $0  wlan0mon"
  	exit 1
fi

INTERFACE="$1"


echo "[🔍] Buscando interfaz inalámbrica..."
if ip link show "$INTERFACE" > /dev/null 2>&1; then
    echo "[✅] Interfaz encontrada: $INTERFACE"
else
    echo "[❌] Interfaz $INTERFACE no encontrada. Abortando."
    exit 1
fi

# Verificar si ya está en modo monitor
if iwconfig "$INTERFACE" | grep -i "Mode:Monitor" > /dev/null; then
    echo "[ℹ️] $INTERFACE ya está en modo monitor. No se requiere acción."
    exit 0
fi

echo "[⚠️] Deteniendo procesos que interfieren (NetworkManager, wpa_supplicant)..."
sudo airmon-ng check kill

echo "[⚙️] Activando modo monitor con airmon-ng..."
sudo airmon-ng start "$INTERFACE"

# Verificación final
NEW_INTERFACE=$(iw dev | awk '/Interface/ {print $2}' | grep "$INTERFACE" || echo "$INTERFACE")

echo ""
echo "[📡] Verificando estado de la interfaz..."
iwconfig "$NEW_INTERFACE"

echo ""
echo "[✅] Modo monitor activo en: $NEW_INTERFACE"
