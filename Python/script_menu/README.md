Script para acessar editores de código
Esse o meu primeiro script transformado em executável, a ideia era desenvolver um menu simples para acessar dois dos meus editores de código favoritos, Vscode e SublimeText.

import pyautogui
import pyautogui as escolha_opcao
opcao =  pyautogui.confirm('CLique no botão desejado', buttons = ['Vscode', 'Sublime Text'])
vs_code = '//home//neybackes//Desktop//code.desktop'
if opcao == 'Vscode':
    escolha_opcao.hotkey('win')
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('vscode')
    escolha_opcao.sleep(2)    
    escolha_opcao.press('Enter')
else:
    escolha_opcao.hotkey('win')
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('sublimetext')
    escolha_opcao.sleep(2)
    escolha_opcao.press('Enter')    
Executável
Para criar o executável utilizei a biblioteca pyinstaller

pyinstaller -D -F -n main -c "script_menu.py"