#Receber um valor n (número inteiro não negativo) e imprimir n vezes os dois primeiros
#caracteres de uma string dada. Se a string tiver menos de dois caracteres, imprime a
#string n vezes.

palavra = "teste"
n =  abs(int(input("Informe o número de cópias: ")))
for value in range(n):
      if len(palavra) < 2:
          print(palavra)
      else:
          print(palavra[:2])