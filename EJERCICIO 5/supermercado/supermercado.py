class Cliente:
    def __init__(self, nro_cliente, nombre, monto):
        self.nro_cliente = nro_cliente
        self.nombre = nombre
        self.monto = monto

    def __repr__(self):
        return f"Cliente({self.nro_cliente}, {self.nombre}, ${self.monto})"

class Trabajador:
    def __init__(self, nro_trabajador, nombre):
        self.nro_trabajador = nro_trabajador
        self.nombre = nombre

    def __repr__(self):
        return f"Trabajador({self.nro_trabajador}, {self.nombre})"

class Caja:
    def __init__(self, numero_caja, trabajador):
        self.numero_caja = numero_caja
        self.trabajador = trabajador
        self.recaudacion = 0.0
        self.clientes_atendidos = 0
        self.cola_clientes = []

    def agregar_cliente(self, cliente):
        self.cola_clientes.append(cliente)

    def procesar_clientes(self):
        while self.cola_clientes:
            cliente = self.cola_clientes.pop(0)
            self.recaudacion += cliente.monto
            self.clientes_atendidos += 1
            print(f"[Caja {self.numero_caja}] {self.trabajador.nombre} atendió a {cliente.nombre} (${cliente.monto})")

    def clientes_por_atender(self):
        return len(self.cola_clientes)

    def __repr__(self):
        return (f"Caja {self.numero_caja} | Trabajador: {self.trabajador.nombre} | "
                f"Recaudación: ${self.recaudacion} | Atendidos: {self.clientes_atendidos} | "
                f"Por atender: {self.clientes_por_atender()}")

class Supermercado:
    def __init__(self):
        self.cajas = []

    def agregar_caja(self, numero_caja, trabajador):
        self.cajas.append(Caja(numero_caja, trabajador))

    def agregar_cliente_a_caja_mas_libre(self, cliente):
        if not self.cajas:
            print("No hay cajas disponibles.")
            return
        caja_mas_libre = min(self.cajas, key=lambda c: c.clientes_por_atender())
        caja_mas_libre.agregar_cliente(cliente)
        print(f"Cliente {cliente.nombre} asignado a Caja {caja_mas_libre.numero_caja} con {caja_mas_libre.trabajador.nombre}")

    def procesar_todas_las_cajas(self):
        for caja in self.cajas:
            caja.procesar_clientes()

    def mostrar_estado_cajas(self):
        for caja in sorted(self.cajas, key=lambda c: c.numero_caja):
            print(caja)

def ingresar_clientes_manualmente(supermercado):
    print("\n--- Ingreso manual de clientes (escribí 'salir' para terminar) ---")
    while True:
        nombre = input("Nombre del cliente (o 'salir'): ").strip()
        if nombre.lower() == "salir":
            break
        try:
            nro = int(input("Número de cliente: "))
            monto = float(input("Monto a pagar: "))
            nuevo_cliente = Cliente(nro, nombre, monto)
            supermercado.agregar_cliente_a_caja_mas_libre(nuevo_cliente)
        except ValueError:
            print("⚠️ Datos inválidos. Intente nuevamente.")
        print()

# Ejemplo de uso
if __name__ == "__main__":
    supermercado = Supermercado()

    # Aqui agregamos cajas y trabajadores
    nombres_trabajadores = ["Laura", "Carlos", "Ana", "Javier", "Elena", "Pablo", "Sonia", "Mateo"]
    for i in range(1, 9):
        supermercado.agregar_caja(i, Trabajador(i, nombres_trabajadores[i - 1]))

    # Agregamos clientes automáticamente
    clientes_ejemplo = [
        (201, "Luis", 250), (202, "Marta", 130), (203, "Jorge", 70),
        (204, "Cecilia", 90), (205, "Sofía", 150), (206, "Pedro", 180),
        (207, "Lucía", 120), (208, "Agustín", 300), (209, "Valeria", 160),
        (210, "Gabriel", 95), (211, "Marina", 105), (212, "Ricardo", 200),
        (213, "Natalia", 80), (214, "Emilia", 170)
    ]
    for nro, nombre, monto in clientes_ejemplo:
        supermercado.agregar_cliente_a_caja_mas_libre(Cliente(nro, nombre, monto))

    print("\n--- Estado antes de ingresar clientes manuales ---")
    supermercado.mostrar_estado_cajas()

    # Ingresar clientes manualmente en bucle
    ingresar_clientes_manualmente(supermercado)

    print("\n--- Estado antes de procesar ---")
    supermercado.mostrar_estado_cajas()

    print("\n--- Procesando clientes ---")
    supermercado.procesar_todas_las_cajas()

    print("\n--- Estado final después de procesar ---")
    supermercado.mostrar_estado_cajas()
