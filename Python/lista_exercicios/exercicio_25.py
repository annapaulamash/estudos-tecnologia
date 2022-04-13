#Ordenar uma lista de acordo com o 2o elemento (lista de listas)

lista = [["A", 43], ["B", 12], ["C", 23], ["D", 8], ["E", 19]]

lista_ordenada = sorted(lista, key = lambda x: x[1]) 

print(lista_ordenada)