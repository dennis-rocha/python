"""Busca sequencial não é necessário que a lista esteja ordenada,
no entanto, ela irá percorrer todos os elementos da lista até encontrar
o elemento que está procurando"""

def BuscaSeq(lista, item):
    pos=0
    x=False
#while para percorrer a minha lista -> enquanto 'pos' for menor que 'tamanho da lista' E NÃO é falso então:
    while pos<len(lista) and not x:
        if lista[pos] == item:
            x=True
        else:
            pos=pos+1
    return x

#minha lista não tem o item 7, no entanto passei como parâmetro para testar o algoritmo
lista = [10, 63, 1, 9, 8, 36, 5, 2, 95, 27]
print(lista)
print ("=============================")
print(BuscaSeq(lista, 36))
print(BuscaSeq(lista, 7))