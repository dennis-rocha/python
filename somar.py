def ReceberNota():
#DECLARAÇÃO DAS VARIAVEIS
    nota=[]
    media=0
    
    for i in range(4):
        nota.append(float(input(f'Digite a nota {i+1} do aluno: ')))

    for i in range(len(nota)):
        media=media+nota[i]

    return media
# INICIO DO PROGRAMA
nome = input('Digite o nome do aluno: ')

nota=ReceberNota()

print ('O aluno(a): {} tirou a nota: {}'.format(nome,nota/4))