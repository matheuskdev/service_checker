from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from PortScan.PortScanner import PortScanner

app = FastAPI()

# Configurando CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Altere isso para a origem específica da sua página (por exemplo, ["http://localhost:8000"])
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/scan/{host}/{ports}")
def scan_ports_route(host: str, ports: str):
    try:
        results = PortScanner.scan_ports(host, ports)
        return {"results": results}
    except ValueError as e:
        return {"error": str(e)}, 400

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
