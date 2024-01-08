import socket
import time
from typing import List

class Scan:
    def __init__(self, host: str, ports: List[int]) -> None:
        self.host = host
        self.ports = ports
        self.client = None

    def check_port(self, port):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.settimeout(5)
            code = self.client.connect_ex((self.host, port))
            result = {"port": port, "status": "OPEN" if code == 0 else "CLOSED", "code": code}
        except socket.error as e:
            result = {"port": port, "status": "ERROR", "error": str(e)}
        except Exception as e:
            result = {"port": port, "status": "ERROR", "error": str(e)}
        finally:
            if self.client:
                self.client.close()
            return result

    def check_all_ports(self):
        results = []
        for port in self.ports:
            result = self.check_port(port)
            results.append(result)
            time.sleep(1)
        return results


