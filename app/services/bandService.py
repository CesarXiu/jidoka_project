import time
from threading import Thread
from app.models.band import Banda

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

def actualizar_item(posicion, nuevo_estatus):
    """
    Actualiza el estatus de un producto en una posición específica.
    
    :param posicion: La posición del producto (1-21).
    :param nuevo_estatus: El nuevo estatus que se asignará al producto.
    """
    try:
        banda.actualizar_item(posicion, nuevo_estatus)
        return {"mensaje": "Estatus actualizado con éxito"}
    except ValueError as e:
        return {"error": str(e)}, 400 
    