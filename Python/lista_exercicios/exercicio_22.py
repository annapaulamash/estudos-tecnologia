#Imprimir o segundo maior elemento de uma lista

lista = ["abc", "abcuu", "abcdef", "avd"]

posicao_maior = lista.index(max(lista, key=len))
lista.pop(posicao_maior)
print(max(lista, key=len))