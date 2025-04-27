from src.dominio.modelo import Cajero, Cliente
from src.uses_case.caja_banco import CajaBanco

class TestCajaBanco:
    @staticmethod
    def main():
        # Crear cajero (generará datos aleatorios)
        cajero = Cajero(id=100)
        caja = CajaBanco(cajero)

        # Crear 5 clientes con datos aleatorios
        for i in range(1, 6):
            cliente = Cliente(id=i)
            caja.agregar_cliente(cliente)

        # Atender clientes
        caja.atender_clientes()

if __name__ == "__main__":
    TestCajaBanco.main()
