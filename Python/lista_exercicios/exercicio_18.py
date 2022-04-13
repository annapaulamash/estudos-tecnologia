#Verificar se uma letra é vogal ou consoante

def teste_vogal(letra):
    vogais = "a, e, i, o, u"
    if letra in vogais:
        return("A letra {} é uma vogal".format(letra))
    return("A letra {} é uma vogal".format(letra))
import os
letra = input("Informe uma letra: \n")
os.system("clear")
print(teste_vogal(letra))