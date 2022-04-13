#Juntar duas listas (numa terceira), ordenar os valores e dizer seu tamanho

lista_um = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_dois = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

nova_lista = sorted(lista_um + lista_dois)

print("Éssa é a nova lista {} com um tamanho de {} posições ".format(nova_lista, len(nova_lista)))
