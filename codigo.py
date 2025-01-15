import pyautogui
pyautogui.PAUSE = 0.5
import time

# Passo 1 : Abrir o sistema da empresa
    # Sistema : https://dlp.hashtagtreinamentos.com/python/intensivao/login
    # Abrir o Navegador
pyautogui.press("win") # Pressiona a tecla Windows do teclado
pyautogui.write("Crhome") # Escreve a palavra 
pyautogui.press("enter")

  # Escolher o usuario
time.sleep(2) # Esperar 2 segundos
pyautogui.click(x=789, y=597) # Seleciona posição na tela e clica com o mouse

time.sleep(2) # Esperar 2 segundos
pyautogui.click(x=237, y=61)

    # Entrar no sistema da empresa
time.sleep(2) # Esperar 2 segundos
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)


# Passo 2 : Fazer login
pyautogui.click(x=709, y=406)
time.sleep(2)
pyautogui.write("testeautomacao@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456789")
pyautogui.press("tab")
pyautogui.press("enter")


# Passo 3 : Importar a base de dados dos produtos
import pandas as pd
tabela = pd.read_csv("produtos.csv")

print (tabela)
time.sleep(2)


# Passo 4 : Cadastrar 1 produto
for linha in tabela.index:
    pyautogui.click(x=684, y=289)
    
    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo)) # str transforma em string 
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":  # nan Not a Number
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(10000)

# Passo 5 : Repetir o passo 4 ate acabar todos os produtos
