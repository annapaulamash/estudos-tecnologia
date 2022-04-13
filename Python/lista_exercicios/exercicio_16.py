#Escreva um programa para contar quantas vezes um determinado número aparece
#numa lista. Leia a lista de números e o número a ser comparado. 
# Forneça a lista de números, separados por vírgula

n = [int(n) for n in input("Informe os valores reparados por vírgula: ").split(",")]
n_alvo = int(input("Infomre o numero a ser comparado: "))

contador =  n.count(n_alvo)
print("O número {} aparece {} vezes na lista".format(n_alvo, contador))