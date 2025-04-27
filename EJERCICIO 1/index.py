from Ejercicio1.tads.pila import Pila
from Ejercicio1.tads.cola import Cola
from Ejercicio1.dominio.clientes import Cliente

def probar_pila():
    print("Prueba de Pila")
    pila = Pila()
    c1 = Cliente('Ernesto','Normal')
    c2 = Cliente('Juan','Preferente')
    c3 = Cliente('Jose','Preferente')
    pila.push(c1)
    pila.push(c2)
    pila.push(c3)
    print("Top:", pila.top())
    print("Size:", pila.size())
    print("Pop:", pila.pop())
    # print("Reverse:", pila.reverse().elementos)
    print("Reverse:", [str(cliente) for cliente in pila.reverse().elementos])


def probar_cola():
    print("\nPrueba de Cola")
    cola = Cola()
    c1 = Cliente('Ernesto','Normal')
    c2 = Cliente('Juan','Preferente')
    c3 = Cliente('Jose','Preferente')
    cola.push(c1)
    cola.push(c2)
    cola.push(c3)
    print("Top:", cola.top())
    print("Size:", cola.size())
    print("Pop:", cola.pop())
    #print("Reverse:", cola.reverse().elementos)
    print("Reverse:", [str(cliente) for cliente in cola.reverse().elementos])


if __name__ == "__main__":
    probar_pila()
    probar_cola()
