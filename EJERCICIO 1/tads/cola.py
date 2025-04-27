class Cola:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        if not self.isEmpty():
            return self.elementos.pop(0)
        return None

    def isEmpty(self):
        return len(self.elementos) == 0

    def top(self):
        if not self.isEmpty():
            return self.elementos[0]
        return None

    def size(self):
        return len(self.elementos)

    def reverse(self):
        nueva_cola = Cola()
        nueva_cola.elementos = list(reversed(self.elementos))
        return nueva_cola

    def pushAll(self, otraCola):
        for elemento in otraCola.elementos:
            self.push(elemento)
