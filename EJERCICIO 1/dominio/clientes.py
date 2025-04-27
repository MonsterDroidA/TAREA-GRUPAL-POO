class Cliente:
    def __init__(self, nombre, tipo="Normal"):
        self.nombre = nombre
        self.tipo = tipo

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"
