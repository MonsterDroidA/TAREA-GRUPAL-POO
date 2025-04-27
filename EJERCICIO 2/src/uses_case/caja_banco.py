
class CajaBanco:
    def __init__(self, cajero):
        self.cola = []
        self.cajero = cajero

    def agregar_cliente(self, cliente):
        self.cola.append(cliente)

    def atender_clientes(self):
        while self.cola:
            cliente = self.cola.pop(0)
            print(
                f"[Cajero {self.cajero.id}] {self.cajero.nombres} "
                f"atiende a {cliente.nombres} (ID: {cliente.id}, "
                f"Género: {cliente.genero})"
            )
