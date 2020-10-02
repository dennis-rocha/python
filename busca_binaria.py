""" IMPORTANTE! Busca Binária é ideal para listas extensas
Para a busca binária é necessário que a lista esteja ordenada! Pois, o algoritmo
irá 'quebrar' a lista ao meio e então comparará se é o item que está procurando
ou não. Caso não seja, então efetuará uma comparação se é maior ou menor que o meio da lista.
E então executará o comando repetidamente até que seja satisfeita a ação ou até chegar no fim das 
divisões sem encontrar o elemento.
"""

def BuscaBinaria(lista, item):
#alpha = primeiro elemento da lista que é 0 e omega = ultimo elemento da lista
    alpha = 0
    omega = len(lista) - 1
    found = False

    while alpha <= omega and not found: #enquanto primeiro elemento menor ou igual ao ultimo elemento E NÃO falso então
        meio = (alpha + omega) // 2 #cria a variavel meio e divide a lista
        if lista[meio] == item: #se lista[no meio] for igual ao item                        """IMPORTANTE!"""
            found = True # foi encontrado. found se torna verdadeiro e encerra o while  | Passo a passo da
        else: #se o item não for igual ao meio então                                    |execução do algoritmo
            if item < lista[meio]: #se o item for menor que a lista [no meio]           |nas ultimas linhas
                omega = meio - 1 #o ultimo elemento recebe o valor da variavel meio - 1 |
            else: #se o item NÃO for menor que a lista no meio então                    |
                alpha = meio + 1 #o primeiro elemento recebe o valor do meio + 1        |
    return found # retorno do se o item foi encontrado ou não (true or false)           |
                                                                                     
#Crei uma lista ordenada com list comprehension e passei como parâmetro um elemento verdadei e outro falso
lista = [x*2 for x in range(0,20) if x % 2 == 0]
print (lista)
print ("=====================================")
print (BuscaBinaria(lista, 3))
print (BuscaBinaria(lista, 28))

"""
Passo a passo da execução do algoritmo
|lista= [1,2,3,4,5] | item= 4
|meio=(1+5)/2 -> '3'
|item é o meio? -> Ñ
|item é <ou= meio? -> Ñ
|lista[1]=meio -> 3
|meio=(3+5)/2 -> '4'
|item é o meio? SIM
|retorna True
"""  