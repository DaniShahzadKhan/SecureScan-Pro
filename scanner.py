import socket
from services import SERVICES, RISK_LEVEL

def scan_target(target, start_port=1, end_port=100):
    open_ports = []

    print(f"\nScanning {target}...\n")

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)

            result = sock.connect_ex((target, port))

            if result == 0:
                service = SERVICES.get(port, "Unknown")
                risk = RISK_LEVEL.get(port, "Low")

                print(f"[OPEN] Port {port:<5} {service:<15} Risk: {risk}")

                open_ports.append((port, service, risk))

            sock.close()

        except Exception:
            pass

    return open_ports