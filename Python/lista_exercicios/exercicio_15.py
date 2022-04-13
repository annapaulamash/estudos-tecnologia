#Verificar se uma string começa com "ab". Se começar, escreve a string, senão escreva
#a string com "ab"na frente

palavra = "teste"

if palavra.startswith("ab"):
    print(palavra)
else:
    print("ab" + palavra)