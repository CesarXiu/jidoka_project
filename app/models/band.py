from .item import Item  # Importa la clase Item

class Banda:
    def __init__(self, size=21):
        self.size = size
        self.productos = [None] * size  # Inicializa la banda vacía
        self.product_id = 1  # Contador de productos generados

    def avanzar(self):
        # Desplaza los productos a la derecha
        for i in range(self.size - 1, 0, -1):
            self.productos[i] = self.productos[i - 1]
        
        # Inserta un nuevo producto en la primera posición
        self.productos[0] = Item(id=f"{self.product_id}", estatus="ok")
        self.product_id += 1  # Incrementa el ID del próximo producto

    def obtener_estado(self):
        # Convierte los objetos Item a diccionarios para exportar el estado
        return {"productos": [producto.to_dict() if producto else None for producto in self.productos]}
    
    def actualizar_item(self, posicion, nuevo_estatus):
        """
        Actualiza el estatus de un producto en una posición específica.
        
        :param posicion: La posición del producto (1-21).
        :param nuevo_estatus: El nuevo estatus que se asignará al producto.
        """
        if 1 <= posicion <= self.size:
            index = posicion - 1  # Convertir a índice basado en 0
            if self.productos[index]:
                self.productos[index].estatus = nuevo_estatus
            else:
                # Si no hay un producto en esa posición, se puede crear uno nuevo
                self.productos[index] = Item(id=f"{self.product_id}", estatus=nuevo_estatus)
                self.product_id += 1
        else:
            raise ValueError(f"Posición inválida: {posicion}. Debe estar entre 1 y {self.size}.")