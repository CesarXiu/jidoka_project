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
        self.productos[0] = {"id": f"{self.product_id}", "estatus": "ok"}
        self.product_id += 1  # Incrementa el ID del próximo producto

    def obtener_estado(self):
        return {"productos": self.productos}
