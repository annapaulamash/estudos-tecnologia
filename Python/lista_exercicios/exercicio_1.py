#Calcular o volume de ume esfera, onde v = 4/3 Pi r³. Mostre o volume com 2 casas decimais.
from math import pow
raio = int(input("Digite o valor do raio da esfera: "))
volume = pow(raio, 3)
volume = (volume * 4) / 3
print("O volume da esfera é de {:.2f}".format(volume))