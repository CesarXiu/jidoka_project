import time
from threading import Thread
from app.model import Banda

banda = Banda()

def iniciar_banda():
    def run():
        while True:
            banda.avanzar()
            time.sleep(30)  # Simula el avance cada 30 segundos
    
    thread = Thread(target=run, daemon=True)
    thread.start()

def obtener_banda():
    return banda.obtener_estado()