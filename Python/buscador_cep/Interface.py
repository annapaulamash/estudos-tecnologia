from Fuctions import buscar_cep, status_code
from tkinter import *

def interface():    

    #criar interface gráfica com o tkinter    
    root = Tk() #começo
    root.title('Buscador de Cep') #titulo
    sub_title = Label(root, text= """
    Essa aplicação foi desenvolvida para práticar o uso de uma API e sua funcionalidades""") #Subtitulo da minha aplicação
    sub_title.grid(row=0, column=1) #colocar o subtitulo na tela
    #capturar valor de entrada do usuaio
    cep_entrada = Entry(root, width=20) #criar caixa de entrada
    cep_entrada.grid(row=6, column=0)

    def clicar():    
      cep = cep_entrada.get()
      resultado = buscar_cep(cep)
      resultado_label = Label(root,justify=LEFT,wraplength=300,text=resultado)
      resultado_label.grid(row=7, column=0)
    meu_botao = Button(root, text='Buscar', command=clicar)
    meu_botao.grid(row=6, column=1)
    root.geometry("300x300")#tamanho da tela
    root.mainloop() #final
        

    
    

