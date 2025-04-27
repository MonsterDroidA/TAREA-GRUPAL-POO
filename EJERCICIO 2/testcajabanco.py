from dominio.cliente import Cliente
from dominio.cajero import Cajero
from banco.banco2 import Banco

class TestCajaBanco:

    @classmethod
    def main(cls):
        banco = Banco()

        cajeros = [
            Cajero("Angy"),
            Cajero("Paul")
        ]

        nombres_clientes = ["Enoc", "Frank", "Francisco", "Angela", "Damaris"]
        for nombre in nombres_clientes:
            cliente = Cliente(nombre)
            banco.ingresar_cliente(cliente)

        banco.atender_clientes(cajeros)


if __name__ == "__main__":
    TestCajaBanco.main()
