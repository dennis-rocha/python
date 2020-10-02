class Somar:
    def __init__ (self, valor, id):
        self.var = valor

    def calcular (self, var, id):

        if id != 1:
            var += var
        else:
            var -= var

        return var

numero1=Somar(100, 9)
print(numero1)