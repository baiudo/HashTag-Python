import pyautogui
# pyautogui -> biblioteca para automação de mouse e teclado
# pyautogui.click -> Clica na posição do mouse
# pyautogui.write -> Escreve o texto na posição do mouse
# pyautogui.press -> Pressiona uma tecla específica
# pyautogui.hotkey -> Pressiona uma combinação de teclas
import time
# time -> biblioteca para manipulação de tempo
# time.sleep -> Pausa a execução do código por um determinado tempo
import pandas
# pandas -> biblioteca para manipulação de dados

pyautogui.PAUSE = 0.5  # Pausa de 0.5 segundo entre os comandos

# Passo 1 - Entrar no sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Abrir o edge
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')
# Inserir a URL
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(3)  # Espera 3 segundos para a página carregar

# Passo 2 - Fazer login
#Inserir email
pyautogui.click(x=552, y=360)  # Clica no campo de email
pyautogui.write('meuemail@gmail.com')  # Email de teste, o site não salva os dados
# Inserir senha
pyautogui.press('tab')  # Move para o campo de senha
pyautogui.write('minhasenha')  # Senha de teste, o site não salva os dados
# Clicar no botão de login
pyautogui.press('enter')  # Pressiona Enter para fazer login

time.sleep(3)  # Espera 3 segundos para o login ser processado

# Passo 3 - Importar base de dados
tabela = pandas.read_csv('produtos.csv')  # Lê o arquivo CSV com os dados dos produtos

# Passo 4 - Cadastrar 1 produto
for linha in tabela.index:
    pyautogui.click(x=563, y=244)  # Clica no botão de cadastrar produto

    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)

    pyautogui.press('tab')

    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)

    pyautogui.press('tab')

    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)

    pyautogui.press('tab')

    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)

    pyautogui.press('tab')

    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)

    pyautogui.press('tab')

    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)

    pyautogui.press('tab')

    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)

    pyautogui.press('enter')  # Envia o produto pro sistema

    pyautogui.scroll(10000)  # Rola a página para cima para limpar o formulário

# Passo 5 - Repetir para todos os produtos
