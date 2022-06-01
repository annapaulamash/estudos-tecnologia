from turtle import width
from Functions import buscar_cep, status_code
import PySimpleGUI as sg

def principal():
    sg.theme('Black')
    layout = [
        [sg.Text('Buscador de CEP', size=(15, 1), font=('Helvetica', 25), text_color='#f8f9fc')],
        [sg.Text('Digite o CEP', size=(15, 3), font=('Helvetica', 15), text_color='#ff7a00')],
        [sg.InputText(size=(15, 1), font=('Helvetica', 15), key='input_cep',)],
        [sg.Button('BUSCAR', size=(13, 1), font=('Helvetica', 15), button_color=('#ff7a00', '#f8f9fc'))]        
    ]
    return sg.Window('Principal', layout=layout,finalize=True)

def janela_princial():
    janela = principal()
    while True:
        window,avent,values = sg.read_all_windows()
        if window == janela and avent == sg.WIN_CLOSED:
            break
        if window == janela and avent == 'BUSCAR':
            if values['input_cep'] == '':
                sg.popup('Preencha o campo! \n O campo não pode ficar em branco.')
            elif len(values['input_cep']) < 8:
                sg.popup('CEP inválido!\nDigite 8 digitos!')
            else:
                cep = values['input_cep']
                resposta = buscar_cep(cep)
                sg.popup(resposta)
            
          

