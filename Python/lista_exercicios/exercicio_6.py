#Receber um nome de arquivo (nome e extensão) e imprimir somente a extensão.

arquivo = input("Informe o nome do arquivo: ")
ext = arquivo.rfind('.')
print("A extensão do arquivo é:",arquivo[ext:])
