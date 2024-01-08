from typing import List
from PortScan.Scan import Scan

class PortScanner:
    @staticmethod
    def scan_ports(host: str, ports: str) -> List[dict]:
        try:
            ports_list = [int(p) for p in ports.split(',')]
            scanner = Scan(host, ports_list)
            results = scanner.check_all_ports()
            return results
        except ValueError:
            raise ValueError("Invalid port numbers")