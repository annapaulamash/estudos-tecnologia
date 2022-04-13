#Receber o primeiro e o último nome de uma pessoa e imprimir em ordem reversa com
#um espaço entre eles.

p_nome, s_nome =  (input(str()) for _ in range(2))
completo = [s_nome[::-1], p_nome[::-1]]
print(', '.join(completo))