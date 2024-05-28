import pyautogui
import time
import pandas as pd
import pyperclip

# 1 - Acessar sistema da empresa
pyautogui.press("win")
pyautogui.write("brave")
time.sleep(1)
pyautogui.press("enter")

time.sleep(1)
pyautogui.write("https://pages.exemplo.com/compras-mes-sistema")
pyautogui.press("enter")

time.sleep(5)

# 2 - Fazer Login no sistema
pyautogui.click(x=953, y=350)
pyautogui.write("peixotodanielsp@gmail.com")
pyautogui.click(x=894, y=421)
pyautogui.write("abacateabacaxi123")
pyautogui.click(x=925, y=497)
time.sleep(5)

# 3 - Baixar a base de dados
pyautogui.click(x=499, y=336)
time.sleep(1)
pyautogui.click(x=590, y=420)
time.sleep(5)
pyautogui.click(x=1081, y=715)
time.sleep(2)
# 4 - Calcular os indicadores

# importar base de dados
tabela = pd.read_csv(r"C:\Users\danie\Downloads\Compras.csv", sep=";")

# calculo de indicadores


# total gasto
total_gasto = tabela["ValorFinal"].sum()
# quantidade
quantidade = tabela["Quantidade"].sum()
# preço medio
preco_medio = total_gasto / quantidade
# 5 - Enviar o email 
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/0/#all")
pyautogui.press("enter")
time.sleep(5)

pyautogui.click(x=84, y=175)
time.sleep(2)
# Preencher e-mail
pyautogui.write("exemplo@gmail.com")
time.sleep(1)
pyautogui.press("tab") # seleciona email
time.sleep(1)
pyautogui.press("tab") # campo de assunto
time.sleep(1)
pyperclip.copy("Relatório de Compras")
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

pyautogui.press("tab") # Campo do email
time.sleep(1)
texto = f'''
Prezados,

Segue o relatório de compras

Total Gasto: R${total_gasto:,.2f}
Quantidade de Produtos: {quantidade}
Preço Médio: R${preco_medio:,.2f}

Qualquer dúvida é só falar.
Att., Daniel
'''
# Copia o texto e cola com caracteres especiais
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# enviar
pyautogui.hotkey("ctrl", "enter")









