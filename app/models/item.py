class Item :
    def __init__(self, id, estatus):
        self.id = id
        self.estatus = estatus # "ok", "report" o "stopped"

    def to_dict(self):
        return {
            'id': self.id,
            'estatus': self.estatus
        }