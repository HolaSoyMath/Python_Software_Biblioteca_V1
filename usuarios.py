from random import randint
from menu import *

def tamanho_usuario(): # Verificar a quantidade de linhas escritas no arquivo txt
    """Calcula o tamanho do arquivo 'Users.txt'.\n
    return --> Quantidade de linhas no arquivo"""
    tamanho = 0
    with open('Users.txt', 'r') as arquivo:
        for i in arquivo:
            tamanho += 1
    return tamanho

def lista_usuarios(): # Criar uma lista com todos os usuários presentes no arquivo txt
    lista_existente = []
    with open('Users.txt', 'r') as arquivo:
         for linha in arquivo:
            lista_existente.append(linha)
    return lista_existente

def cadastrar_usuario(): # Cadastrar um NOVO usuário no arquivo Users
    '''Cadastrar um usuário no arquivo de usuários.'''
    tamanho = tamanho_usuario()
    lista_users = lista_usuarios()
    nome = str(input('Qual o nome a ser cadastrado? (Digite 0 para voltar ao menu principal) ')).title().strip()
    if nome[0] == '0':
        return int(nome)
    codigo = gerar_codigo_usuario(nome)
    lista_users.append(f'{tamanho+1};{nome};{codigo}\n')
    return lista_users
    
def escrever_usuarios(plista_users): # Escrever a lista de usuários no arquivo Users
    '''Escrever o parametro lista no arquivo txt.\n
    param lista_users --> Lista de itens a serem escritos no arquivo "Users.txt"'''
    with open('Users.txt', 'w') as arquivo:
        for linha in plista_users:
            arquivo.write(linha)

def gerar_codigo_usuario(pnome):
    '''Gerar código para o novo usuário.\n
    param nome --> Nome do usuário.'''
    parte2 = parte3 = ''
    parte1 = pnome[:3].upper()
    for i in range(3):
        parte2 = str(parte2 + str(randint(0,9)))
    for i in range(3):
        parte3 = parte3 + chr(randint(65, 90))
    return parte1 + parte2 + parte3

def print_usuarios(pvoltar=False, ptamanho=False):
    '''Printar toda a lista de usuários com seu devido índice.\n
    param voltar --> Indicar se deve aparecer o menu voltar. (Padrão: False).\n
    param tamanho --> Indicar o tanto de linhas do arquivo. (Padrão: False.'''
    lista_user = lista_usuarios()
    print(f'|{"ID":^4}{"Nome Usuario":^102}{"Cód. Usuario":^12}|')
    for user in lista_user:
        user = user.replace('\n','')
        linha_user = user.split(';')
        print(f'|{linha_user[0]:<3}.{linha_user[1]:^102}{linha_user[2]:^12}|')
        linha_user = []
    if pvoltar == True:
        print(f'|\033[31m{"0":<3}.{"  Voltar"}\033[m{"|":>107}')
    linha()
    if ptamanho == True:
        return len(lista_user)
    
def editar_usuario(pindice):
    # Alocar corretamente o indice que sera modificado
    pindice -= 1
    # Gerar uma lista de todos os usuarios
    lista_user = lista_usuarios()
    linha()
    # Escolher para qual nome será modificado
    resp = str(input('Deseja modificar para qual nome? ')).title().strip()
    # criar uma variavel do tipo lista para modificar apenas os campos necessários
    linha_alterar = lista_user[pindice]
    linha_split = linha_alterar.split(';')
    # Gerar um novo código para o usuário
    codigo = gerar_codigo_usuario(resp)
    # Substituir informações na lista da linha
    linha_split[1] = resp
    linha_split[2] = codigo
    # Substituir informação no indice da lista principal
    lista_user[pindice] = f'{linha_split[0]};{linha_split[1]};{linha_split[2]}\n'
    # Escrever a lista no arquivo de usuários
    escrever_usuarios(lista_user)
