#!/bin/bash

# Verificar si se pasaron los 2 argumentos requeridos
if [ "$#" -ne 2 ]; then
  echo "❌ Uso incorrecto."
  echo "✅ Uso correcto: $0 <nombre_salida> <interfaz_monitor>"
  echo "Ejemplo: $0 captura_01 wlan0mon"
  exit 1
fi

# Asignar argumentos a variables
OUTPUT_NAME=$1
INTERFACE=$2

# Ejecutar airodump-ng
sudo airodump-ng -w "$OUTPUT_NAME" --output-format csv "$INTERFACE"

