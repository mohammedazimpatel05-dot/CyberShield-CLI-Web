import socket
import json
import sys
from datetime import datetime

def scan_target(target_host, ports=[21, 22, 80, 443, 3306, 8080]):
    print(f"[*] Starting Security Scan on: {target_host}")
    results = {"target": target_host, "timestamp": str(datetime.now()), "open_ports": []}
    
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5)
        status = s.connect_ex((target_host, port))
        if status == 0:
            print(f"[+] Port {port}: OPEN")
            results["open_ports"].append(port)
        s.close()
        
    with open("scan_results.json", "w") as f:
        json.dump(results, f, indent=4)
    print("[*] Scan complete. Saved to scan_results.json")

if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    scan_target(host)
