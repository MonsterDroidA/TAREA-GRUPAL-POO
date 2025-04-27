class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        if not self.isEmpty():
            return self.elementos.pop()
        return None

    def isEmpty(self):
        return len(self.elementos) == 0

    def top(self):
        if not self.isEmpty():
            return self.elementos[-1]
        return None

    def size(self):
        return len(self.elementos)

    def reverse(self):
        nueva_pila = Pila()
        nueva_pila.elementos = list(reversed(self.elementos))
        return nueva_pila

    def pushAll(self, otraPila):
        for elemento in otraPila.elementos:
            self.push(elemento)
