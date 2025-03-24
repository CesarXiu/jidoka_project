import time

class Operational:
    """
    Clase para manejar la disponibilidad operativa de la banda transportadora.
    """

    def __init__(self, planned_hours=8):
        """
        Inicializa los contadores de tiempo de operación y detención.
        """
        self.OP_TIME = 0  # Tiempo operativo en minutos
        self.OP_STOP = 0  # Tiempo de paro en minutos
        self.PLANNED_TIME = planned_hours * 60  # Convierte horas a minutos
        self.last_start_time = None  # Momento en que se inició la operación
        self.stop_start_time = None  # Momento en que inició un paro
        self.OVERTIME = 0  # Tiempo extra trabajado en minutos
        self.PR_RET = 0  # Productos retrabajados
        self.PR_INSP = 0  # Productos inspeccionados

    def production_start(self):
        """
        Inicia la producción y calcula el tiempo de paro si hubo una detención previa.
        """
        if self.stop_start_time is not None:  
            # Calcula el tiempo detenido y lo acumula en OP_STOP
            self.OP_STOP += (time.time() - self.stop_start_time) / 60
            self.stop_start_time = None  # Resetea el tiempo de paro

        self.last_start_time = time.time()  # Marca el inicio de la operación

    def production_stop(self):
        """
        Detiene la producción y calcula el tiempo de operación acumulado.
        """
        if self.last_start_time is not None:
            # Calcula el tiempo operando y lo suma a OP_TIME
            self.OP_TIME += (time.time() - self.last_start_time) / 60
            self.last_start_time = None  # Resetea el inicio de operación
            # Calculamos overtime si se excedió el tiempo planificado
            if self.OP_TIME > self.PLANNED_TIME:
                self.OVERTIME = self.OP_TIME - self.PLANNED_TIME
        
        self.stop_start_time = time.time()  # Marca el inicio del paro
    
    def OP_Overtime(self):
        """
        Calcula el tiempo extra trabajado (overtime).
        
        :return: Tiempo extra trabajado en minutos.
        """
        if hasattr(self, 'OVERTIME'):
            return round(self.OVERTIME, 2)
        return 0
    
    def OP_Availability(self):
        """
        Calcula la disponibilidad operativa.
        
        :return: Porcentaje de disponibilidad operativa.
        """
        total_time = self.OP_TIME + self.OP_STOP
        return (self.OP_TIME / total_time) * 100 if total_time > 0 else 100
    
    def register_inspected_product(self):
        """
        Registra un producto inspeccionado.
        """
        self.PR_INSP += 1

    def report_reworked_product(self):
        """
        Registra un producto que ha sido retrabajado.
        """
        if self.PR_INSP > 0:  # Asegura que haya productos inspeccionados
            self.PR_RET += 1

    def Rework_Rate(self):
        """
        Calcula la tasa de retrabajo.
        
        :return: Porcentaje de productos retrabajados con respecto a los inspeccionados.
        """
        return (self.PR_RET / self.PR_INSP) * 100 if self.PR_INSP > 0 else 0
    
    def get_times(self):
        """
        Devuelve los tiempos operativos y de paro, junto con el tiempo extra.
        """
        return {
            "OA": round(self.OP_Availability(), 2), # Porcentaje de disponibilidad operativa
            "OT": round(self.OVERTIME, 2),  # Minutos extra
            "RR": round(self.Rework_Rate(), 2) # Porcentaje de retrabajo
        }
