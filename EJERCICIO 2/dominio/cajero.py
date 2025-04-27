class Cajero:
    def __init__(self, nombre):
        self.nombre = nombre

    def atender_cliente(self, cliente):
        print(f"La persona {cliente.nombre} ha sido atendida por {self.nombre}.")
