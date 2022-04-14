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