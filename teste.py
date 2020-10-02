def Nota ():
        nota = int(input("Digite a nota: "))

        return nota 

nome = input ("Digite o nome do aluno: ")
nota1=Nota()
nota2=Nota()
nota3=Nota()
nota4=Nota()

print ("O nome do aluno é {0}".format(nome))
print ("A média é {0}".format((nota1+nota2+nota3+nota4)/4))

lista = []