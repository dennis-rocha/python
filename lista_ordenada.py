def BubbleSort(lista):
    n= len(lista)-1
    for j in range(n-1):
        for i in range(n-1):
            if lista[i]>lista[i+1]:
                temp=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=temp
                print(lista)

lista=[10, 63, 1, 9, 8, 36, 5, 2, 95, 27]
BubbleSort(lista)