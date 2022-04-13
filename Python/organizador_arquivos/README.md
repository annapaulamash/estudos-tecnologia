# **Exercício com a bilbioteca OS**

## _Proposta_:

A ideia deste escript é utilizar as funcionalidades e métodos da biblioteca OS para desenvolver um organizador de arquivos.
O objetivo é organizar os arquivos dentro de uma nova pasta utilizando uma função para ler a extensões dos arquivos dentro diretório.

~~~Python
#Definindo as extensões a serem encontradas
arq_ext= ['.py','.txt']
#Função para encontrar a extensão do arquivo
def pegar_extensao(nome):
    index = nome.rfind('.')
    return nome[index:]         
~~~
De início do script deve identificar as pastas a ser salva, caso esta já exista o programa mantem o direitorio e transfere os arquivos com as extensões alvo.
~~~Python
def criar_pasta(diretorio, nome_pasta):
    pasta =  os.path.join(diretorio, "{}".format(nome_pasta))  
    if not os.path.isdir(pasta):
        os.mkdir(pasta)  
    nomes_arquivos = os.listdir(diretorio)
    nova_pasta = ''
    for arquivo in nomes_arquivos:
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            # extensão do arquivo com letras minúsculas
            extensao = str.lower(pegar_extensao(arquivo))
            if extensao in arq_ext:
                nova_pasta = pasta
                velho = os.path.join(diretorio, arquivo)
                novo = os.path.join(nova_pasta, arquivo)
                os.rename(velho, novo) 