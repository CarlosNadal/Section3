import csv
import sys

def clean_header(row):
    return [col.strip() for col in row]

def parse_csv(csv_path):
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)

    # Buscar dónde empieza la tabla de APs y estaciones
    ap_start = next((i for i, row in enumerate(rows) if "BSSID" in row), None)
    station_start = next((i for i, row in enumerate(rows) if "Station MAC" in row), None)

    if ap_start is None:
        raise ValueError("No se encontró encabezado válido con 'BSSID'.")

    headers_ap = clean_header(rows[ap_start])
    aps = []
    for row in rows[ap_start + 1 : station_start]:
        if not row or len(row) < len(headers_ap):
            continue
        ap = dict(zip(headers_ap, row))
        if ap.get("ESSID") is not None:
            aps.append(ap)

    headers_sta = []
    stations = []
    if station_start:
        headers_sta = clean_header(rows[station_start])
        for row in rows[station_start + 1 :]:
            if not row or len(row) < len(headers_sta):
                continue
            sta = dict(zip(headers_sta, row))
            stations.append(sta)

    return aps, stations

def select_best_target(aps, stations):
    # Convertir potencia a int y filtrar APs sin potencia
    aps = [ap for ap in aps if ap.get("Power") and ap["Power"] != '']
    aps = sorted(aps, key=lambda ap: int(ap["Power"]), reverse=True)

    # Map BSSID a lista de clientes conectados
    clients_per_ap = {}
    for sta in stations:
        bssid = sta.get("BSSID", "(not associated)").strip()
        if bssid != "(not associated)":
            clients_per_ap.setdefault(bssid, []).append(sta)

    print("\n🔍 Mejores objetivos y sus clientes conectados:\n")
    for ap in aps[:10]:
        bssid = ap["BSSID"]
        clients = clients_per_ap.get(bssid, [])
        print(f"📡 ESSID: {ap['ESSID'] or '<oculto>'} | BSSID: {bssid}")
        print(f"   Canal: {ap['channel']} | Señal: {ap['Power']} dBm | Cifrado: {ap['Privacy']} / {ap['Authentication']}")
        print(f"   Beacons: {ap['# beacons']} | IVs: {ap['# IV']}")
        print(f"   Clientes conectados: {len(clients)}")

        if clients:
            print("   ► Clientes:")
            for c in clients:
                print(f"      - MAC: {c['Station MAC']} | Señal: {c['Power']} | Paquetes: {c['# packets']}")
        print("-" * 50)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 best_target.py <archivo.csv>")
        sys.exit(1)

    try:
        aps, stations = parse_csv(sys.argv[1])
        select_best_target(aps, stations)
    except Exception as e:
        print(f"❌ Error procesando CSV: {e}")
