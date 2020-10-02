class Conta:
# O CAMNDO INIT É PRECISO TER DOIS UNDERLINES EX: _ _init_ _
    def __init__ (self, nome, numero):
        self.cliente=nome
        self.num=numero
        self.saldo = 0.0

    def Saldo (self):
        return self.saldo

    def getCliente (self):
        return self.cliente

    def Depositar (self, valor):
        self.saldo += valor

conta1 = Conta("Dennis", 1)
conta1.Depositar(100.0)
print(conta1.getCliente())
print(conta1.Saldo())

conta2 = Conta("Priscila", 2)
conta2.Depositar(200.0)
print(conta2.getCliente())
print(conta2.Saldo())
