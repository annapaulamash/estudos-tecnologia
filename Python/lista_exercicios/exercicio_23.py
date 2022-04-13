#Separar os pares dos ímpares, colocando em duas listas diferentes. Devem ser lidos
#10 valores. Ao final diga quantos elementos tem cada lista e imprima seus valores.
par = []
impar = []
for value in range(1, 11):
    if value % 2 == 0:
        par.append(value)
    else:
        impar.append(value)
        
print("Temos {} valores pares: {}".format(len(par), par))
print("Temos {} valores impares: {}".format(len(impar), impar))