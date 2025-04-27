from collections import deque

class Banco:
    def __init__(self):
        self.cola = deque()

    def ingresar_cliente(self, cliente):
        self.cola.append(cliente)
        print(f"{cliente.nombre} ingresó a la cola.")
        
    def atender_clientes(self, cajeros):
        cajero_count = len(cajeros)
        i = 0
        while self.cola:
            cliente = self.cola.popleft()
            cajero = cajeros[i % cajero_count]  
            cajero.atender_cliente(cliente)
            i += 1

