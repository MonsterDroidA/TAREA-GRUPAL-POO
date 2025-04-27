from collections import deque

# Clase para representar una tarea
class Tarea:
    def __init__(self, area=None, descripcion=None):
        self.area = area
        self.descripcion = descripcion

    def getArea(self): return self.area
    def setArea(self, area): self.area = area
    def getDescripcion(self): return self.descripcion
    def setDescripcion(self, descripcion): self.descripcion = descripcion

    def __str__(self):
        return f"Área: {self.area}, Descripción: {self.descripcion}"

# Clase para representar la información de un empleado
class Empleado:
    def __init__(self, codigo=None, nombre=None):
        self.codigo = codigo
        self.nombre = nombre
        self.tareas = deque()

    def getCodigo(self): return self.codigo
    def setCodigo(self, codigo): self.codigo = codigo
    def getNombre(self): return self.nombre
    def setNombre(self, nombre): self.nombre = nombre

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def procesar_tarea(self):
        if self.tareas:
            tarea = self.tareas.popleft()
            print(f"Tarea procesada del empleado {self.codigo} - {self.nombre}: {tarea}")
        else:
            print(f"Empleado {self.codigo} - {self.nombre} no tiene tareas para procesar.")

    def cantidad_tareas(self):
        return len(self.tareas)

# Clase que representa la empresa y gestiona la lista de empleados
class Empresa:
    def __init__(self):
        self.empleados = []

    def getEmpleados(self): return self.empleados
    def setEmpleados(self, empleados): self.empleados = empleados

    def agregar_empleado(self, codigo, nombre):
        empleado = Empleado(codigo, nombre)
        self.empleados.append(empleado)
        self.empleados.sort(key=lambda e: e.codigo)  # Ordenado por código

    def obtener_empleado_menos_tareas(self):
        return min(self.empleados, key=lambda e: e.cantidad_tareas())

    def ingresar_nueva_tarea(self, area, descripcion):
        tarea = Tarea(area, descripcion)
        empleado = self.obtener_empleado_menos_tareas()
        empleado.agregar_tarea(tarea)
        print(f"Tarea asignada al empleado {empleado.codigo} - {empleado.nombre}")

    def procesar_tareas_rango(self, desde=15, hasta=30):
        print(f"\nProcesando tareas de empleados del {desde} al {hasta}")
        for empleado in self.empleados:
            if desde <= empleado.codigo <= hasta:
                while empleado.tareas:
                    empleado.procesar_tarea()

    def mostrar_empleados(self):
        print("\nLista de empleados y sus tareas:")
        for e in self.empleados:
            print(f"Empleado {e.codigo} - {e.nombre} - Tareas: {e.cantidad_tareas()}")

# Ejemplo de uso
if __name__ == "__main__":
    empresa = Empresa()

    # Lista de empleados
    empleados_data = [
        (10, "Carlos"), (15, "Alejandro"), (20, "Sara"),
        (25, "Gabriela"), (30, "Nasus"), (35, "Luna")
    ]

    # Agregarlos a la empresa
    for codigo, nombre in empleados_data:
        empresa.agregar_empleado(codigo, nombre)

    # Agregar tareas
    tareas_predefinidas = [
        ("Contabilidad", "Revisar balances"),
        ("Sistemas", "Actualizar sistema"),
        ("RRHH", "Entrevistas"),
        ("Ventas", "Llamar clientes"),
        ("Legal", "Revisar contratos"),
        ("Producción", "Supervisar línea"),
        ("Base de datos", "Respaldar base de datos"),
        ("RRHH", "Revisar currículums"),
        ("Finanzas", "Preparar informe"),
        ("Ventas", "Seguimiento a cotizaciones"),
        ("Marketing", "Diseñar campaña"),
        ("Soporte", "Resolver ticket"),
        ("Auditoria", "Auditoría interna")
    ]

    for area, descripcion in tareas_predefinidas:
        empresa.ingresar_nueva_tarea(area, descripcion)

    empresa.mostrar_empleados()

    # Procesar tareas en el rango 15 al 30
    empresa.procesar_tareas_rango(15, 30)

    empresa.mostrar_empleados()

    # Permitir ingreso manual de nuevas tareas
    while True:
        opcion = input("\n¿Deseas ingresar una nueva tarea? (s/n): ").lower()
        if opcion != "s":
            break
        area = input("Área de la tarea: ")
        descripcion = input("Descripción de la tarea: ")
        empresa.ingresar_nueva_tarea(area, descripcion)
        empresa.mostrar_empleados()

