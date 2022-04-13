 #Receber uma sequência de números separados por vírgula e gerar uma lista e uma
#tupla com eles.
n = [int(n) for n in input("Informe os valores reparados por vírgula: ").split(",")]
print("LIsta: ",n)
print("Tupla: ",(*n,))