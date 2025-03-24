import time
from threading import Thread
from app.models.band import Banda

banda = Banda()
banda_activa = False  # Variable de control para iniciar/detener la banda
reportados = {}  # Diccionario para rastrear elementos reportados y su tiempo de reporte

def iniciar_banda():
    global banda_activa
    banda_activa = True  # Activa la banda

    def run():
        while banda_activa:
            verificar_reportados() # Verifica si hay elementos reportados que exceden el tiempo permitido
            banda.avanzar()
            time.sleep(30)  # Simula el avance cada 30 segundos

    thread = Thread(target=run, daemon=True)
    thread.start()

def detener_banda():
    global banda_activa
    banda_activa = False  # Detiene la banda

def obtener_banda():
    return banda.obtener_estado()

def actualizar_item(posicion, nuevo_estatus):
    """
    Actualiza el estatus de un producto en una posición específica.
    
    :param posicion: La posición del producto (1-21).
    :param nuevo_estatus: El nuevo estatus que se asignará al producto.
    """
    global reportados, banda_activa
    try:
        producto = banda.productos[posicion - 1]
        if producto:
            # Validar transiciones de estado
            estado_actual = producto.estatus
            if nuevo_estatus == "ok" and estado_actual not in ["report", "stopped"]:
                raise ValueError(f"No se puede cambiar de '{estado_actual}' a 'ok'")
            if nuevo_estatus == "report" and estado_actual != "ok":
                raise ValueError(f"No se puede cambiar de '{estado_actual}' a 'report'")
            if nuevo_estatus == "stopped" and estado_actual != "report":
                raise ValueError(f"No se puede cambiar de '{estado_actual}' a 'stopped'")

            # Actualizar el estado del producto
            banda.actualizar_item(posicion, nuevo_estatus)

            # Manejar el diccionario de reportados
            if nuevo_estatus == "report":
                reportados[producto.id] = {"time": time.time(), "posicion": posicion}
                print(f"Producto con ID {producto.id} reportado en posición {posicion}.")
            elif nuevo_estatus == "ok":
                if producto.id in reportados:
                    reportados.pop(producto.id, None)
                # Reactivar la banda si no quedan elementos en estado "stopped"
                if not any(banda.productos[i - 1] and banda.productos[i - 1].estatus == "stopped" for i in range(1, banda.size + 1)):
                    iniciar_banda()
                    print("Todos los elementos liberados. La banda se ha reactivado.")
            elif nuevo_estatus == "stopped":
                reportados[producto.id] = {"time": time.time(), "posicion": posicion}

            return {"mensaje": "Estatus actualizado con éxito"}
        else:
            raise ValueError(f"No hay producto en la posición {posicion}")
    except ValueError as e:
        raise e  # Re-lanza el error para que sea capturado por el bloque `except` en la ruta

    
def verificar_reportados():
    """
    Verifica si algún producto reportado ha excedido el tiempo permitido (1.5 minutos).
    Si es así, cambia su estado a 'stopped' y detiene la banda.
    """
    global banda_activa
    tiempo_actual = time.time()
    for producto_id, data in list(reportados.items()):
        if tiempo_actual - data["time"] > 90:  # 1.5 minutos = 90 segundos
            # Busca el producto en la banda por su ID
            for posicion, producto in enumerate(banda.productos, start=1):
                if producto and producto.id == producto_id:
                    banda.actualizar_item(posicion, "stopped")
                    detener_banda()  # Detiene la banda
                    print(f"Producto con ID {producto_id} en posición {posicion} pasó a 'stopped' y la banda se detuvo.")
                    break