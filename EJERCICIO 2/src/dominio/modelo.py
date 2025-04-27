from faker import Faker

class Persona:
    fake = Faker('es_ES')  # Datos en español

    def __init__(self, id: int):
        self.id = id
        perfil = self.fake.simple_profile()
        self.nombres = perfil['name']
        self.genero = "Masculino" if perfil['sex'] == 'M' else "Femenino"
        self.direccion = perfil['address']

class Cliente(Persona):
    def __init__(self, id: int):
        super().__init__(id)

class Cajero(Persona):
    def __init__(self, id: int):
        super().__init__(id)
