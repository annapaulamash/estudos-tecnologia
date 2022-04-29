

import pyautogui
import pyautogui as escolha_opcao

#link de acesso download
link = 'https://docs.google.com/spreadsheets/d/1AToabuB_d9s2tv6rWxSQyzbFuqUuj8aCYeQ_GD6EJPg/edit?usp=drive_web&ouid=101865441184343255661'

#funções
def menu_princial():
    menu =  pyautogui.confirm('Dados Financeiros.\n CLique na opção desejada', buttons = ['Download planilha', 'Calculo rendimentos', 'Salvar', 'Enviar email'])

    return opcao(menu)
#opcões do script
def opcao(menu):
    if menu == 'Download-Planilha':
            escolha_opcao.hotkey('ctrl', 'alt', 't')
            escolha_opcao.sleep(2)
            escolha_opcao.write('google-chrome')
            escolha_opcao.press('enter') 
            escolha_opcao.write('https://docs.google.com/spreadsheets/d/1AToabuB_d9s2tv6rWxSQyzbFuqUuj8aCYeQ_GD6EJPg/edit?usp=drive_web&ouid=101865441184343255661')    
            escolha_opcao.sleep(2)
            escolha_opcao.hotkey('ctrl', 'v')
            escolha_opcao.press('enter')
            escolha_opcao.sleep(10)
            escolha_opcao.click(x=88, y=121)
            escolha_opcao.click(x=228, y=376)
            escolha_opcao.click(x=411, y=375)
            escolha_opcao.alert(text='Donwload Concluido', title='', button='OK')
    elif menu == 'Calculo-Rendimentos':

        import pandas as pd
        df = pd.read_excel()

        juros = []
        for value in (df['Juros (%)']):
            juros.append(value)
        poupanca = []
        for value in (df['Poupança']):
            poupanca.append(value)
        cdb = []
        for value in (df['CDB']):
            cdb.append(value )
        tm = []
        for value in (df['Título Imobiliário']):
            tm.append(value )
        prev = []
        for value in (df['Previdência']):
            prev.append(value )
        poupanca_j = []
        for value in (df['Poupança']):
            poupanca_j.append(value * df['Juros (%)'].loc[0])
        cdb_j = []
        for value in (df['CDB']):
            cdb_j.append(value * df['Juros (%)'].loc[1])
        tm_j = []
        for value in (df['Título Imobiliário']):
            tm_j.append(value * df['Juros (%)'].loc[2])
        prev_j = []
        for value in (df['Previdência']):
            prev_j.append(value * df['Juros (%)'].loc[3] )

        total_investido = zip(poupanca, cdb, tm, prev)

        t_investido = [a + b + c + d for (a, b, c, d) in total_investido]

        total_juros = zip(poupanca_j, cdb_j, tm_j, prev_j)

        t_juros = [a + b + c + d for (a, b, c, d) in total_juros]

        df['Valor Investido'], df['Rendimentos'] = t_investido, t_juros

                 
     

        
        

    
#chamda da função

menu_princial()


    





       

