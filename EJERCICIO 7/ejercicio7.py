class Cliente:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.ordenes = []

    def agregar_orden(self, orden):
        self.ordenes.append(orden)


class Item:
    def __init__(self, descripcion, peso, precio):
        self.descripcion = descripcion
        self.peso = peso
        self.precio = precio

    def precio_por_cantidad(self, cantidad):
        return self.precio * cantidad

    def obtener_peso(self, cantidad):
        return self.peso * cantidad


class DetalleOrden:
    def __init__(self, item, cantidad, tipo_impuesto=0.15):
        self.item = item
        self.cantidad = cantidad
        self.tipo_impuesto = tipo_impuesto

    def calc_subtotal(self):
        return self.item.precio_por_cantidad(self.cantidad)

    def calc_peso(self):
        return self.item.obtener_peso(self.cantidad)

class Pago:
    def __init__(self, monto):
        self.monto = monto


class Credito(Pago):
    def __init__(self, monto, fecha, numero, tipo, autorizado):
        super().__init__(monto)
        self.fecha = fecha
        self.numero = numero
        self.tipo = tipo
        self.autorizado = autorizado

class Efectivo(Pago):
    def __init__(self, monto, moneda):
        super().__init__(monto)
        self.moneda = moneda

class Cheque(Pago):
    def __init__(self, monto, nombre, identif_banco, autorizado):
        super().__init__(monto)
        self.nombre = nombre
        self.identif_banco = identif_banco
        self.autorizado = autorizado


class Orden:
    def __init__(self, fecha, estado):
        self.fecha = fecha
        self.estado = estado
        self.detalles = []
        self.pagos = []

    def agregar_detalle(self, detalle):
        self.detalles.append(detalle)

    def agregar_pago(self, pago):
        self.pagos.append(pago)

    def calc_impuesto(self):
        impuesto = sum(detalle.calc_subtotal() * detalle.tipo_impuesto for detalle in self.detalles)
        return impuesto

    def calc_total(self):
        subtotal = sum(detalle.calc_subtotal() for detalle in self.detalles)
        return subtotal + self.calc_impuesto()

    def calc_peso_total(self):
        peso_total = sum(detalle.calc_peso() for detalle in self.detalles)
        return peso_total

#Simulación #1

#crear cliente
cliente = Cliente("Juan Pérez", "Calle Falsa 123")

#crear ítems
item1 = Item("Laptop", 2.5, 1000)
item2 = Item("Mouse", 0.1, 50)

#crear orden
orden = Orden("2025-04-25", "Nueva")

#crear detalles de orden
detalle1 = DetalleOrden(item1, 1)  # 1 Laptop
detalle2 = DetalleOrden(item2, 2)  # 2 Mouse

#detalles a la orden
orden.agregar_detalle(detalle1)
orden.agregar_detalle(detalle2)

#agregar orden
cliente.agregar_orden(orden)

#total de impuesto
print(f"Impuesto de la orden: ${orden.calc_impuesto():.2f}")
print(f"Total de la orden: ${orden.calc_total():.2f}")
print(f"Peso total de la orden: {orden.calc_peso_total()} kg")

#realiza pago
pago = Efectivo(1100, "USD")
orden.agregar_pago(pago)

#mostra los detalles
print(f"\nCliente: {cliente.nombre}")
print(f"Dirección: {cliente.direccion}")
print(f"Número de órdenes: {len(cliente.ordenes)}")
print(f"Pagos realizados: {len(orden.pagos)}")
