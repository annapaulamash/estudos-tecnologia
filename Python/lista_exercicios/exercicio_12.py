#Retornar a diferença entre um dado número e 17. Se o número for maior que 17,
#retorne o valor absoluto do dobro da diferença.


n = int(input("Informe um número: "))

diferenca = abs(17 - n)

if diferenca > 17:
    print(diferenca + diferenca)
else:
    print(diferenca)